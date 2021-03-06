import time

import sys
import subprocess
import util
import os
import random
import json
import re
import fuzz as F
import fuzzingbook.Parser as P

def usage():
    print("""
check_precision.py <golden grammar> <inferred grammar> <non-instrumented executable> <working directory> <count attempts>
    Used for checking the precision of the provided grammar. We generate inputs
    using the golden grammar, identify the semantically valid ones using non
    instrumented executable, and run these valid inputs against a parser using
    inferred grammar. The output is how many of these valid inputs were parsed
    by the parser.
    <golden grammar>:   The externally provided grammar that is used to generate inputs.
    <inferred grammar>: The inferred grammar from program
    <non-instrumented executable>: The non instrumented executable to first verify the inputs against.
    <working-directory>: a working directory
    <count attempts>: Number of valid inputs to generate
    """)
    sys.exit(0)

def main(args):
    if not args or args[0] == '-h': usage()
    errors = []
    with open(args[0]) as f:
        golden = json.load(f)
    ggrammar = golden['[grammar]']
    gstart = golden['[start]']

    with open(args[1]) as f:
        mined = json.load(f)
    mgrammar = mined['[grammar]']
    mstart = mined['[start]']

    command = args[2]
    directory = args[3]
    count = int(args[4])
    key = args[5]
    os.makedirs(directory, exist_ok=True)
    fuzzer = F.LimitFuzzer(ggrammar)
    i = 0
    correct = 0
    seen = set()
    timeout = 0
    while True:
        try:
            v = fuzzer.fuzz(gstart)
            if not v.strip(): continue
            if v in seen: continue
            seen.add(v)
            fn = '%s/%s.input.x' % (directory, key)
            with open(fn, 'w+') as f:
                print(v, end='', file=f)
            o = util.do([command, fn])
            if o.returncode != 0:
                continue
            else:
                #print(repr(v))
                i += 1
                o = util.do(["python3", "./src/parser.py", args[1], fn], timeout=60)
                if o.returncode == 0:
                    correct += 1
                    #print('parsed. %d/%d (timeout: %d)' % (correct, i, timeout))
                else:
                    print('not parsed %d/%d (timeout: %d)' % (i - correct, i, timeout), o.stdout, o.stderr)
        except RecursionError:
            print('recursion.')
            pass
        except subprocess.TimeoutExpired:
            timeout += 1
            print('timedout.')
            pass
        if i >= count: break
    with open("%s/%s.precision_" % (directory, key), 'w+') as f:
        print('%s result: %d/%d (timeout: %d)' % (key, correct, i, timeout), file=f)
    return errors

def process_token(i):
    if i and i[0] == '<' and ' ' in  i:
        return i.split(' ')[0] + '>'
    elif i and i[0] == '<':
        return i
    else:
        return repr(i)

if __name__ == '__main__':
    main(sys.argv[1:])

