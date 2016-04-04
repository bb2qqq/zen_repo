![TEST Debug Flow](/Users/zen1/zen/pythonstudy/tech_lab/TEST_skills/software_test_debug_flow.png)

## Useful Coverage test tools
1. Sofeware name: coverage  
Usage: `coverage html target_file.py`


## Write Testable Softwares

* clean code
* If not clean, refactor
* Should always be able to describe what a module does or how it interact with other code
* no extra threads
* no swamp of global variables
* modules should have unit tests
* when applicable support fault injection
* assertions, assertions, assertions

### Assertions
Notices:
1. Assertions are not used for error handling.
2. NO SIDE EFFECTS
3. NO SILLY ASSERTIONS [assert (1+1) == 2]

Why assertions?
* make code self-checking
* make code fail early, closer to the bug
* assertion lives in interface between modules can assign blame
* document assumptions, preconditions, postconditions, invariants

Statistics
GCC: 9000 assertions
LLVM: 13000 assertions (1.4M line, so 1 assertion per 110 lines)

Tips:
python -O will ignore assertions in code


Enable assertions in production?
When doing daily jobs, NASA engineer enables assertion. Only when the spacecraft trying to land Mars, they disable the assertions.

### Principles

* Interfaces that span trust boundaries are special.  
They must be tested on the full range of representable values.
* good test suite has good test coverage, but good test coverage doesn't necessarily prove a test suite is good.  
Because people can tweak a test suite to get a better test coverage instead of trying to improve its quality.  


### Test coverage
Try to trigger all functions in the code to be tested.  
If not 100% percent functiosn were tested. There maybe dead code or negligence in the test.  
Test coverage just make sure all your code been executed at least once, it can give you evidence that your code is bug free.  

Three day to day coverage metrics.
    * line coverage
    * statement coverage
    * branch converage

Other metrics:

  * MC/DC coverage(Modified condition and decision coverage)  
      This coverage will test whether all conditions can independently affect the outcome of the decision.  
      If some condition can't do that, which means they could be redundant, or there could be bugs counter designer's intention.

  * Path coverage(Test all the possible path)  
      It should covers every possible logic path of the code(Though at many situation impossible to cover all).  
      This is an example: ![path_coverage](/Users/zen1/zen/zen_repo/tech_lab/python_mania/TEST_skills/pictures/path_coverage.png)

  * Boundary value coverage(1 off bug is a common bug that can be find out by boundary value coverage)

  * Interleaving coverage and sychronazition coverage are used to test concurrent software.

### What does code that doesn't get covered mean?
There are three possibilities when this happened:  

1. The code is infeasible, such as bug check functiosn that never detect false conditions. In this condition, we comment the code in a specified way so that coverage test suit will ignore them.
2. code not worth covering, like the last 2 lines in the example below:

        res = formatDisk()
        if res == "ERROR":
            abort()
3. test suite inadequate.  
    * We can improve it to make it cover more code.
    * Or we could ignore it if we think it's OK, especially when we think it's OK for customers to be the first people who run the code.(Like in some web applications)


### Anecdote
SQLite is an small open source database which can easily be embedded in other softwares. It was used by Aribus, Dropbox, Apple devices and Android phones.  

It has:
* 77.6K lines of code
* & 91,392K lines of TEST code
* & which means the TEST code is **1000x** times more than functional code
* It achieved 100% branch coverage, 100% MC/DC coverage, with a large number of random testing, boundary values are used, contains a tons of assertions, passed valgrind check, integer overflow case tested, and fault injection test were performed.


### Automated whitebox test
According to cs-258 tutor's knowledge, there isn't python automated whitebox test software till the time he made the lecture video.

`Klee` is a software he recommend to try with.
