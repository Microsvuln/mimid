# Replication package for _Mining Input Grammars From Dynamic Control Flow_

**IMPORTANT** This complete source code of this artifact is hosted
[in this Github repository](https://github.com/vrthra/mimid).

Our submission is a tool that implements the algorithm given in the paper
_Mining Input Grammars From Dynamic Control Flow_.
We provide the virtual machine [mimid](https://doi.org/10.5281/zenodo.3876969)
which contains the complete artifacts necessary to
reproduce our experiments. We describe the process of invoking the virtual
machine below.

We also note that if you are unable to download the vagrant box (It is 3 GB)
You can also take a look at the complete worked out example of how to derive
grammar for an example program at [src/PymimidBook.ipynb](https://github.com/vrthra/mimid/blob/master/src/PymimidBook.ipynb).
The [src/PymimidBook.ipynb](https://github.com/vrthra/mimid/blob/master/src/PymimidBook.ipynb)
notebook also contains all the Python experiments in the paper. It can be
viewed either by using the virtual box as explained below, or can be directly
viewed using any of the Jupyter notebook viewers such as VSCode. A
non-interactive version hosted at Github is accessible [from this link](https://github.com/vrthra/mimid/blob/master/src/PymimidBook.ipynb)
(If the load fails, click reload until you can view it).

## Rebuilding the vagrant box

If you want to recreate the virtual box, simply execute `make box-create` in the root directory.

```bash
$ make box-create
```

## Overview

This paper presents a novel general algorithm for mining the input grammar
of a given program. Our algorithm _mimid_ takes a program and a small
set of inputs, and automatically infers a readable (upto) context-free
grammar that captures the input language of the program. Our progarm
relies only on having access to _access patterns_ in the initial input
buffer from different locations in the parser. Our technique works on all
stack based recursive descent input parsers including parser combinators,
and works without program specific heursitics.

We evaluate the grammars obtained by _mimid_ on a variety of subjects.

## Prerequisites

### RAM

All experiments done on a base system with **15 GB RAM**, and the VM was
allocated **10 GB RAM**.

### Setup

First, please make sure that the port 8888 is not in use. Our VM forwards its
local port 8888 to the host machine.

#### Download

Next, please download the vagrant box from the following link:

https://doi.org/10.5281/zenodo.3876969

This produces a file called `mimid.box` which is 2.6 GB in size
(the commands in the host system are indicated by
leading `$` and the other lines indicate the expected output),

```bash
$ du -ksh mimid.box
2.6G  mimid.box
```

and should have the following _md5_ checksum.

```bash
$ md5sum mimid.box
431f6ded243e91dcd5077b00ae2aa9b3 mimid.box
```

#### Importing the box

The vagrant box can be imported as follows:

```bash
$ vagrant box add mimid ./mimid.box
==> box: Box file was not detected as metadata. Adding it directly...
==> box: Adding box 'mimid' (v0) for provider:
    box: Unpacking necessary files from: file:///path/to/mimid/mimid.box
==> box: Successfully added box 'mimid' (v0) for 'virtualbox'!

$ vagrant init mimid
A `Vagrantfile` has been placed in this directory. You are now
ready to `vagrant up` your first virtual environment! Please read
the comments in the Vagrantfile as well as documentation on
`vagrantup.com` for more information on using Vagrant.

$ vagrant up

Bringing machine 'default' up with 'virtualbox' provider...
==> default: Importing base box 'mimid'...
==> default: Matching MAC address for NAT networking...
==> default: Setting the name of the VM: vtest_default_1591177746029_82328
==> default: Fixed port collision for 22 => 2222. Now on port 2200.
==> default: Clearing any previously set network interfaces...
==> default: Preparing network interfaces based on configuration...
    default: Adapter 1: nat
==> default: Forwarding ports...
    default: 8888 (guest) => 8888 (host) (adapter 1)
    default: 22 (guest) => 2200 (host) (adapter 1)
==> default: Running 'pre-boot' VM customizations...
==> default: Booting VM...
==> default: Waiting for machine to boot. This may take a few minutes...
    default: SSH address: 127.0.0.1:2200
    default: SSH username: vagrant
    default: SSH auth method: private key
==> default: Machine booted and ready!
==> default: Checking for guest additions in VM...
==> default: Mounting shared folders...
    default: /vagrant => /path/to/mimid
```

#### Verify Box Import

The commands inside the guest system are indicated by a `vm$ ` prefix.
Anytime `vm$` is used, it means to either ssh into the vagrant box as below, or
if you are already in the VM, use the shell inside VM.

```bash
$ vagrant ssh

vm$ free -g
              total        used        free      shared  buff/cache   available
Mem:              9           0           9           0           0           9
Swap:             1           0           1
```

## A complete example

```bash
vm$ pwd
/home/vagrant
vm$ ls
mimid
c_tables.sh
py_tables.sh
start_c_tests.sh
start_py_tests.sh
startjupyter.sh
taints
toolchains
```

The following are the important files

| File/Directory               | Description                                                                 |
|------------------------------|-----------------------------------------------------------------------------|
| startjupyter.sh              | The script to start Jupyter notebook to view examples. |
| start_py_tests.sh            | Start the _Python_ experiments. |
| py_tables.sh                 | CLI for viewing the results from C experiments. |
| start_c_tests.sh             | Start the _C_ experiments. |
| c_tables.sh                  | CLI for viewing the results from Python experiments. |
| mimid/src/                   | The main _mimid_ algorithm implementation. |
| mimid/Cmimid                 | The modularized _mimid_ implementation (in Python) experiments in _C_. |
| mimid/src/PymimidBook.ipynb  | The detailed _mimid_ notebook which also contains experiments in _Python_. |
| toolchains/                  | The original LLVM and Clang tool chain. |
| taints/                      | The module to instrument C files. |

The most important file here is `mimid/src/PymimidBook.ipynb` which is the
Jupyter notebook that contains the complete algorithm explained and worked out
over two examples: one simple, and the other more complex. It can be
interactively explored using any of the Jupyter notebook viewers including
VSCode or directly using a browser as explained below.

It can also be viewed (read only) directly using the github link [here](https://github.com/vrthra/mimid/blob/master/src/PymimidBook.ipynb)

### Viewing the Jupyter notebook

From within your VM shell, do the following:

```bash
vm$ ./startjupyter.sh
...
     or http://127.0.0.1:8888/?token=ba5e5c480fe4a03d56c358b4a10d7172d2b19ff4537be55e
```

Copy and paste the last line in the host browser. The port `8888` is forwarded
to the host. Click the [src](http://127.0.0.1:8888/tree/src) link from the
browser and within that folder, click the [PymimidBook.ipynb](http://127.0.0.1:8888/notebooks/src/PymimidBook.ipynb)
link. This will let you see the complete set of examples as well as the
Python experiments in an already executed form.

You can either interactively explore the notebook by first clearing the
current values `Kernel>Restart & Clear Output` and executing each cell
one at a time, or by running all the experiments at once by
`Kernel>Restart & Run All`. Other options are also available from menu.


## Starting the experiments

There are two sets of experiments: The Python experiments
(`calc.py`, `mathexpr.py`, `cgidecode.py`, `urlparse.py`, `microjson.py`, `parseclisp.py`)
and the C experiments
(`json.c`, `tiny.c`, `mjs.c`).
We explain the _Python_ part first.

### Python experiments

**IMPORTANT** The system is **very memory intensive**. Hence, do not run the
experiments in parallel (e.g. concurrently from a different shell). If you
do that, you might get a _memory error_.

The following are the Python programs

| Program         | Input Language Kind | Description |
|-----------------|---------------------|-------------|
| `calc.py`       | Context Free        | A simple calculator program.             |
| `mathexpr.py`   | Context Free        | A more complex math expression program which supports functions. |
| `cgidecode.py`  | Regular             | A program to decode CGI encoded strings. |
| `urlparse.py`   | Regular             | A program to parse URLs.                 |
| `microjson.py`  | Context Free        | A program to parse JSON strings.         |
| `parseclisp.py` | Context Free        | A program to parse s-expressions.        |


There are two main ways to run the Python experiments. Either through the
Jupyter notebook as we explained earlier, or if you are on a headless system,
using the command line, which is explained below.

To start the Python experiments, execute the shell command below:

```bash
vm$ ./start_py_tests.sh
```

This will execute the Python experiments embedded in the Jupyter notebook
without requiring a browser, and produce an HTML file `PymimidBook.html`
in the `/home/vagrant` folder which may be viewed offline.

#### Result analysis for Python (CLI)

After running the python experiments using *command line*, the results can be
inspected using the following command line. Note that running it through
Jupyter notebook interface will not produce the `PymimidBook.html` file which
is required for using `py_tables.sh`. In that case, please view the results
directly in the notebook *Results* section.

```bash
vm$ ./py_tables.sh

Precision (Table 1)     Autogram        Mimid
-----------------
calculator.py,  37.5%,  100.0%
mathexpr.py,    26.9%,  97.8%
urlparse.py,    100.0%, 100.0%
cgidecode.py,   47.6%,  100.0%
microjson.py,   47.5%,  98.6%

Recall (Table 2)        Autogram        Mimid
-----------------
calculator.py,  1.6%,   100.0%
mathexpr.py,    0.2%,   93.4%
urlparse.py,    100.0%, 95.0%
cgidecode.py,   34.7%,  100.0%
microjson.py,   0.0%,   93.0%
```

Here, we compare the results from *Autogram* to the results from *mimid*.
What this means is that the grammar inferred by *mimid* for `microjson`
(for example) when used with a grammar based random fuzzer, generated
inputs such that 98.6% of such inputs were accepted by `microjson.py` when
compared to the grammar inferred by *Autogram* that could only produce
(using a grammar fuzzer) 47.5% valid inputs (Table 1).
Similarly, when valid *Javascript* strings were randomly generated using
a fuzzer and the golden grammar for Javascript, 93.0% of such inputs would be
parsed correctly by a parser that uses the grammar mined by *mimid* from
`microjson` when compared to a parser using a grammar mined using *Autogram*
from `microjson` which accepts 0.0% of the inputs (Table 2).

### C experiments

The following are the C programs

| Program         | Input Language Kind | Description |
|-----------------|---------------------|-------------|
| mjs.c           | Context Free        | The embedded Javascript interpreter. |
| tiny.c          | Context Free        | The `tinyC` C compiler. |
| json.c          | Context Free        | A JSON parser. |

The C experiments are not accessible from the Jupyter notebook as it requires
instrumenting the C programs. Further, the set of C programs is intended as
a demonstration of how to use the _mimid_ algorithm in a standalone fashion.

The C experiments are in the directory `mimid/Cmimid`, and the modularized
_mimid_ implementation (in Python) is available under `mimid/Cmimid/src`.

To start the C experiments, execute the shell command below:

```bash
vm$ ./start_c_tests.sh
```

This will execute all the C experiments, and produce results which can be
analyzed as below:

#### Result analysis for C

Note that for `C` there is no *Autogram* implementation available, so
we have nothing to compare against. Hence, the precision and recall is provided
as is. The following command line produces the results (table names are in
correspondence with the paper).

```bash
vm$ ./c_tables.sh
Precision (Table 1)     Mimid
-----------------
mjs     97.5%
tiny    92.8%
json    83.8%

Recall (Table 2)        Mimid
-----------------
mjs     90.5%
json    100.0%
tiny    100.0%
```

As before, what this means is that the grammar inferred by *mimid* for `mjs`
(for example), when used with a random grammar fuzzer, generated inputs such
that 97.5% of such inputs were accepted by `mjs` (Table 1). Similarly, when
valid *Javascript* strings were generated randomly using a golden grammar,
90.5% of such inputs were parsed correctly by a parser that uses the grammar
mined by *mimid* from `mjs` (Table 2).

## How is the algorithm organized

The Jupyter notebook provided has complete documentation of the entire
algorithm. Each method is thoroughly documented,
and executions of methods can be performed to verify their behavior.
Use the Jupyter notebook
[src/PymimidBook.ipynb](https://github.com/vrthra/mimid/blob/master/src/PymimidBook.ipynb)
as the main guide, and for interactive exploration of the algorithms.

The algorithm consists of the following parts. The part in the paper is given
as a heading, and the corresponding parts in Jupyter notebook are noted below.

### Paper: Section 3 _Tracking control flow and comparisons_

1. Instrumenting the source code to track access and control flow.

   Section 1.5 _Rewriting the source code_ in the Jupyter notebook.

2. Running the inputs, and generating access traces.

   Section 1.6 _Generating traces_ in the Jupyter notebook.

### Paper: Section 4 _From traces to parse trees_

3. Extracting the traces to a parse tree.

   Section 1.7 _Mining Traces Generated_ in the Jupyter notebook.

4. Active learning of labelling (Section 4.1, 4.2 in paper)

   Section 1.8 _Generalize Nodes_ in the Jupyter notebook
   Section 4.1 in the paper corresponds to Section 1.8.1 in Jupyter notebook
   Section 4.2 in the paper corresponds to Section 1.8.2 in Jupyter notebook

### Paper: Section 5 _Grammar Inferrence_

5. Generating the grammar from the collected parse trees.

   Section 1.9 _Generating a grammar_ in the Jupyter notebook.

### Paper: Section 6 _Evaluation_

  Section 2 _Evaluation_ in the Jupyter notebook

## How to add a new subject

We discuss how to add Python and C subjects below.

### Adding a new Python program

To add a new Python program, one needs to know what kind of a parer
it has. That is, if it is the traditional recursive descent, or a
parser combinator implementation. Both are discussed below.

#### Adding a traditional recursive descent Python program

**IMPORTANT:** We assume that you have the program as well as the sample inputs.
Both are required for grammar mining. In particular, we can only mine the
features that are exercised by the given set of samples. Instead of the sample
inputs, one can also provide a golden grammar which can be used instead to
generate inputs (that may or may not be accepted by the program --- i.e the
grammar implemented need not be in sync with the golden grammar, but rather,
we can use the golden grammar to explore the implementation --- We only use
accepted inputs for mining).

Ensure that the program has no external calls during parsing such as [shlex](https://docs.python.org/3/library/shlex.html)
or other lexers. For ease of explanation, we assume that you have a single
source file program called `ex.py`. Copy and paste the contents of
`ex.py` in the Jupyter notebook in a cell in the *Our subject programs* section
with the following format:

```
%%var ex_src
# [(
...
# )]
```

where the ellipsis (...) is replaced by the contents of the file `ex.py`.

Next, register it in `program_src` variable as below:

```python
program_src = {
  ...
  'ex.py': VARS['ex_src'],
}
```

Execute all the modified cells so that the variables are correctly populated.

Also, make sure to execute the following fragment in _Generate Transformed Sources_ section

```python
# [(
for file_name in program_src:
    print(file_name)
    with open("subjects/%s" % file_name, 'wb+') as f:
        f.write(program_src[file_name].encode('utf-8'))
    with open("build/%s" % file_name, 'w+') as f:
        f.write(rewrite(program_src[file_name], file_name))
# )]
```

which will produce the original file `mimid/src/subjects/ex.py` and the
instrumented file `mimid/src/build/ex.py`.)

Next, fill in the sample inputs in an array as follows (preferably under
the _Evaluation/Subjects/_ section under an *Ex* heading):

```python
ex_samples = [ . . . ]
```
Again, fill in the ellipsis with the correct values.

Now, grammar mining is as simple as executing the following command

```python
ex_grammar = accio_grammar('ex.py', VARS['ex_src'], ex_samples, cache=False)
```

The `ex_grammar` variable will hold the mined grammar. If there are any errors,
restart and re-execute the Jupyter notebook completely (with the added example).
This will clear away any interfering global state, and execute the example
correctly.

#### Adding a parser combinator example

Adding a new parser combinator is more involved as it requires modification
of the library. In particular, there is no information to be gathered from
the method names as they are generic names such as `curried` and `parse`.
The actual readable names are provided as the variable names of parser objects.

E.g. the actual readable information is present in the variable name `digit`
rather than the method name `any_of` in the below example.

```python
digit = any_of(string.digits)
```

Unfortunately, Python provides no easy way for us to recover the name of the
variable that holds an object from within the object. Hence, we require that
each object that contains a recognizable parser such as `digit` also defines
a `.tag` member variable which provides the name associated as a string.

(While it can be technically done using an AST rewrite automatically, or there
might be other clever ways of recovering the variable name, we have not done
that at this point.)

```python
digit = any_of(string.digits)
digit.tag = 'digit'
```

Hence, one can either reuse the existing parser combinator library in section
_The parsec library_, or use your own combinator library with the `tag`
information for each parser object as given above.

Since adding a new parser combinator library is fairly complex, and may require
additional customization of the library, we do not explore that here. Instead
we assume that you use the parser combinator library given in the Jupyter
notebook itself.

To make the addition simple, please add your example program under
the _A parsec lisp parser_ section, by adding the program `pcex` in the end
under a new cell. Use `%%var pcex_src` line as the first line in that cell
with your parser combinator definitions. Make sure to provide the `.tag` string
to each named parser. Finally, make sure that you define a `main` function
that takes in the string to be parsed as an argument.

E.g.

```python
%%var pcex_src
import string
import json
import sys
import myparsec as pyparsec

ap = pyparsec.char('a')
ap.tag = 'a'
bp = pyparsec.char('b')
bp.tag = 'b'

abparser = ap >> bp
abparser.tag = 'abparser'

def main(arg):
    v = abparser.parse(arg)
    if isinstance(v, pyparsec.Left):
        raise Exception('parse failed')
    return v
```

Next, provide your own samples in the variable `pcex_samples` as we showed
earlier.

Finally, the grammar can be extracted as

```python
pc_grammar = accio_grammar('pcex.py', VARS['pcex_src'], pcex_samples)
```

where the variable `pc_grammar` holds the grammar mined.

### Adding a new C program

First, move into `/home/vagrant/mimid/Cmimid/`. This is the base directory for
C examples.

```bash
vm$ cd ~/mimid/Cmimid
```

Check the targets supported by the `Makefile` as below:

```bash
vm$ make help
```

For subject specific help, use help-subject

E.g.

```bash
vm$ make help-tiny
```

To add a new C program, we assume that the program you have is a single C file
called `ex.c`. The `ex.c` is assumed to read inputs both from `stdin` as well as
as an argument to the program, which is then processed by the parsing function
in your program.

Assuming that your parser entry point is a function
`parse_ex(char* input, char* result)`, copy and paste the following into your
program. (The second parameter `result` is only an example, and is not needed.
All you need is some means to return the parse failure or success).

```C
void strip_input(char *my_string) {
  int read = strlen(my_string);
  if (my_string[read - 1] == '\n') {
    my_string[read - 1] = '\0';
  }
}

int main(int argc, char *argv[]) {
  char my_string[10240];
  char result[10240];
  init_hex_values();
  int ret = -1;
  if (argc == 1) {
    char *v = fgets(my_string, 10240, stdin);
    if (!v) {
      exit(1);
    }
    strip_input(my_string);
  } else {
    strcpy(my_string, argv[1]);
    strip_input(my_string);
  }
  printf("val: <%s>\n", my_string);
  ret = parse_ex(my_string, &result);
  return ret;
}
```

Place the program under `examples/`. Further, provide the golden grammar of
your program as `ex.grammar` under the same directory.

E.g:

```bash
vm$ ls examples/ex.*
examples/ex.c examples/ex.grammar
```

The golden grammar `examples/ex.grammar` is used to generate inputs.

One can also provide sample inputs, in which case, they can be used instead.
In that case, place the program under `examples/` as before. Then, provide
the sample inputs to your program as `ex.input.1`, `ex.input.2` etc. under
the same directory (please follow the `*.input.<n>` naming convention.
It is required for the `make`).

Note that the original abstract target is the following, where `KIND` is set
to `generate` from grammar.

```
build/%.inputs.done: build/%.inputs.done.$(KIND)
    touch $@
```

Since we are providing a set of inputs, we only need to copy.
Hence *edit* the `Makefile` and *add* a new target for this file as below.

```
build/ex.inputs.done: build/ex.inputs.done.copy
    touch $@
```

IMPORTANT: Note that the `KIND` part of the receipt is set to `copy`.

Next, check whether your program has a lexer or a tokenizer. A lexer
reads the input, and splits it into predefined tokens before it is passed
into the program. For an example of a program that uses a lexer,
see `examples/mjs.c` where the lexer is `static int pnext(struct pstate *p)`.
For an example of a program that does not use a lexer, see `examples/cgi_decode.c`
where each character is processed directly by the parser.

If it has a lexer, then edit the `Makefile`, and define a target
`build/ex.events` as below. Note that the `Makefile` syntax requires a
`tab` i.e. (`\t`) before the recipe.


```
build/ex.events: build/ex.json.done
  $(PYTHON) ./src/tokenevents.py build/ex/ > $@_
  mv $@_ $@
```

If it does not use a lexer, then the default `build/%.events`
target will work without modification.

Once this is done, one can mine the grammar and extract the grammar with the
following commands:

```bash
vm$ make build/ex.grammar
vm$ cat build/ex.grammar
```

The precision of the grammar can be extracted with:

```bash
vm$ make build/ex.precision
vm$ cat build/ex.precision
```

Similarly, the recall can be extracted with:

```bash
vm$ make build/ex.fuzz
vm$ cat build/ex.fuzz
```

Note that one can also proceed step by step,

1. First compiling and instrumenting the program:

```bash
vm$ make build/tiny.x
vm$ make build/tiny.d
```

2. Then generating inputs using the provided golden grammar
   (If copying the sample inputs, *edit* the `Makefile` and add a new receipt
   for the inputs as described previously, with the KIND set to `copy` for this
   particular target.)

```bash
vm$ make build/tiny.inputs.done
```

3. Running the instrumented program to collect the traces

```bash
vm$ make build/tiny.json.done
```

4. Extract the `mimid` buffer access events with control flow annotation

```bash
vm$ make build/tiny.events
```

5. Extract the parse trees from the collected events.

```bash
vm$ make build/tiny.tree
```

After this, the following command can be used to view the parse trees generated
using ASCII art.

```bash
vm$ make build/tiny.showtree
```

6. Extract the generalized grammar from the parse trees

```bash
vm$ make build/tiny.mgrammar
```

7. Convert the generalized grammar to a compact EBNF form

```bash
vm$ make build/tiny.grammar
```

After this, the following command can be used to inspect the grammar generated
in a colorized form:

```bash
vm$ make build/tiny.showg
```

8. Convert the grammar to the `fuzzingbook` canonical representation for parsing

```bash
vm$ make build/tiny.pgrammar
```

At this point, one can evaluate the `precision` and `recall` as follows:

**Precision**

```bash
vm$ make build/tiny.precision
```

**Recall**

```bash
vm$ make build/tiny.fuzz
```

We also note that each command line invoked by the make can also be invoked
directly. All command lines take a flat `-h` which provides information on
its argument, and how it is used. We have opted to keep the documentation
in the Jupyter notebook, and simply generate the modules in accordance with
the DRY principle.

E.g Viewing the trees at different stages of generalization.

```bash
vm$ python3 ./src/ftree.py
ftree.py <json file> <tree numbers>*
    Display the selected trees from <json file>
    if <tree numbers> is empty, all trees are shown if not, only selected trees are shown
```

Using it (the first line is the string that was parsed.):

```bash
vm $ python3 ./src/ftree.py build/tiny.tree 1 2 | less -r
o )if ( a < a ); else ; else { ; }}else ; '
'<START>'
+-- '<_real_program_main(1).0>'
    +-- '<parse_expr.0>'
            +-- '<program.0>'
                        |-- '<statement.0>'
...
```

The parse trees in in-between stages can also be inspected:

```bash
vm$ ls build/tiny-*tree*
build/tiny-loop_trees.json  build/tiny-method_trees.json  build/tiny-trees.json
```

For example, the initial parse tree is in `build/tiny-trees.json`. The first
tree before generalization can be viewed as

```bash
vm $ python3 ./src/ftree.py build/tiny-trees.json 0 | less -r
```

The next generalization stage is methods. The result can be seen as

```bash
vm $ python3 ./src/ftree.py build/tiny-method_trees.json 0 | less -r
```

The final generalization stage (copied to `build/tiny.tree`) is `build/tiny-loop_trees.json`
which can be viewed as

```bash
vm $ python3 ./src/ftree.py build/tiny-loop_trees.json 0 | less -r
```

Similarly, any of the in-between grammars can be inspected. For example, the
non-generalized mined grammar is `build/tiny-mined_g.json` which can be viewed
as:

```bash
vm$ cat build/tiny-mined_g.json | jq . -C | less -r
{
  "[start]": "<START>",
    "[grammar]": {
    . . .
  },
  "[command]": "build/tiny.x"
}
```


where `[start]` is the start symbol.

**Grammar Format**

The `[grammar]` is the grammar in the [Fuzzingbook](https://www.fuzzingbook.org/html/Parser.html)
canonical JSON format, where the nonterminals are represented as keys of a
python `dict`, and each nonterminal is associated with a definition represented
by an `list` of `rules`, and each `rule` is again a `list` of tokens, and each
token can either be a nonterminal or a terminal symbol represented as a string.

The `[command]` is the un-instrumented program that
accepts the grammar (The instrumented program from which the grammar was mined
can be obtained by substituting `.x` with `.d`.)

After tokens are generalized, it becomes `build/tiny-general_tokens.json`
(before compaction), which can be viewed as

```bash
vm$ cat build/tiny-general_tokens.json | jq . -C | less -r
```

The defined top level keys are:

```bash
vm$ cat build/tiny.grammar | jq '. | keys'
[
  "[command]",
  "[grammar]",
  "[start]"
]
```

Note that the tree formats are also fixed.

```bash
vm$ cat build/tiny.tree | jq '.[0] | keys'
[
  "arg",
  "original",
  "tree"
]
```

For example, one can access the input file that generated a particular tree (`0`) using:

```bash
vm$ cat build/tiny.tree | jq '.[0].arg' -C
```

The `.original` contains the (un-instrumented) program from which grammar
was mined.

```bash
vm$ cat build/tiny.tree | jq '.[0].original' -C | less -r
```


Finally, tree itself is

```bash
vm$ cat build/tiny.tree | jq '.[0].tree' -C | less -r
```

**Derivation Tree Format**

The tree format is again from the [Fuzzingbook](https://www.fuzzingbook.org/html/Parser.html),
where the derivation tree is represented as a recursive structure with each node
represented by a tuple or pair list with the first element, the
nonterminal that corresponds to that node, and the second element the children
of that node, and remaining elements contain any meta information associated
with the node. The terminal symbols are represented by nodes with empty
children.

## Notes

The complete run (below command line) can take up to 10 hours to complete.

```
vm$ ./start_c_tests.sh && ./start_py_tests.sh
```

