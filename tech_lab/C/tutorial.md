### 疑问
C语言如何写一个(只接受一个参数，但这个参数可以为int或char)的函数？  
没有pointer的struct，内存里的数据如何删除掉。  

### type casting
在C语言里，你可以将一个type转换成另一个type, 基本的syntax是`(type_name) expression`


### char name[] = "Mario"; 和 char \*name = "Mario"; 的区别

简单说来`char name[] = "Mario"` 定义了一个array, array里的元素都在当前scope的stack里。  
而`char *name = "Mario";`定义了一个指针，该指针储存在当前scope的stack里，而它指向的内容"Mario"则存在内存里另外某处（是heap吗？）  

这两种方法，都是现在内存里先生成一个string literal，存放字符串的内容，这个string literal的内容是不应该被改写的。  
`char name[]`会将该literal的内容完全复制到一块新的内存上，你可以任意改写这块内存上的值。  
`char *name`则是申请一小块内存，这一小块内存的类型是一个16进制的long型数字，它的值则是string literal的内存地址。  


[相关讨论](http://stackoverflow.com/questions/1335786/c-differences-between-char-pointer-and-array)


## POINTERS

### Pointer Mechanism
Pointer的本质是指定内存地址的值。
当你将一个pointer指向某个类型的数据，c语言会找到该数据的内存地址，将它的值赋给你指定的指针名。  
而`*ptr`本质上是说，给我拿到我这个`ptr`所指向的内存地址上储存的值。  
在C语言里貌似输入内存地址和正确的值，可以打印出该内存上储存的值，如果类型不对的话，C貌似会把内存地址转换，[相关讨论](http://stackoverflow.com/questions/34542481/whats-the-rules-that-c-converts-address-to-int/34542796#34542796)

> 当你使用`printf("%s")`时，%s会自动做一个对pointer取值的动作，所以你只需把pointer对象传给c，而不是pointer的值。
### Pointer Lexicon
`type *ptr`
	 "a pointer of type named ptr"

`*ptr`
    "the value of whatever ptr is pointed at"

`*(ptr + i)`
    "the value of (whatever ptr is pointed at plus i)"

`&thing`
    "the address of thing"

`type *ptr = &thing`
    "a pointer of type named ptr set to the address of thing"

`ptr++`
    "increment where ptr points"

### Memory Leakage
In C, if you allocate a memory, and there is no pointers pointed to it.  
Then this memory is forgot, we can also call this `memory leakage`.  
Actually, if you just assign things memories but forgot to recollect the memory after the task.  
Then the usable memory space will be decreased. After accumulations by time and iterations. Your program will crash because of lack of memory.  

### Void type
In C, if a function returns nothing, we specified it with a `void` type

### NULL
In C, NULL is a `unset or invalid pointer`, you often use it to determing if a pointer is valid.  
Like `if (my_pointer != NULL) { do_something()}`

### Get address of variable
In C, you directly operate on memory addresses, thus you can print them out, too.  
Remember, what consists basis of computer? Binary! Thus memory address is actually a number!  
We print it with `%p` escaper, and add a `&` symbol before the variable, so explicity tell the compiler we want print the address.  
`&` is the `symbol of get the address`

    \\ CODE
    #include <stdio.h>

    int main(int argc, char *argv[]) {
        int a = 5;
        char *str_array[] = {"LWW", "TCM", "BGG"};
        printf("%p\n", &a);
        printf("%p\n", &str_array);
        return 0;
    };

    \\ RESULT
    0x7fff5113b93c
    0x7fff5113b950

### Arrays or Pointers?
Pointers is something that refers to a particular area of memory，  
You should only use it in these 4 conditions:

1. Ask the OS for a chunk of memory to work with, which includes `struct`.
2. Passing large blocks of memory(like large structs) to functions.
3. Taking the address of a function so to use it as a dynamic callback.
4. Complex Scanning of chunks of memory, such as converting bytes off a socket into data structure, or parsing files.

For nearly everything else when you see others using pointers, they should use arrays.  
In early years, using pointers can boost speed, but nowadays, arrays and pointers have the same speed.  
So no need to optimize on this.  
So, you shall always use array as you can. Pointers optimization is kind of ultimate resolution.  



### Scopes
In C, inside every single round of for loop, it got an isolated scope.  
Take a look of the code below:

    #include <stdio.h>

    int main(int argc, char *argv[])
    {
        char letter = 'a';
        int i = 0;

        for (i=0; i<3; i++) {
            char letter = argv[1][i];
            printf("%c\n", letter);
        };
        printf("%c\n", letter);
        return 0;
    }

    make ex
    ./ex bus

    b
    u
    s
    a

You can see that the `letter` variable inside the `for loop` won't affect the `outside letter variable`.  
And it changes every round.  



### bitwise OR/AND & Logical OR/AND

1. Bitwise operator will excuted all the comparison no matter what,  
meanwhile Logic operator will stop execute when the condition can't be True.

Take an example:
    if x() & y() { //do something }
    if x() && y() { //do something }

The when `x()` evaluates to `false`, the first bitwise operator will continue to run `y()`,  
but the second logical operator statement won't run `y()`, it just stops.  

2. Bitwise operator is faster than logic operator, even if they are in the same speed, it costs less system resource.

3. it seems in C, bitwise operator only works as you expected on int `1` and `0`,  
if you add other types in comparison, it may acts out of your imagination.  
For example. `i^j^k` will be evaluates to true both for `char i='a'; int j=0; int k=0;` and `char i='a'; int j = 1; int k=0;`.

### Tips

Using `for loops` in favour of `while loops`, because `for loop` are harder to break.


### Data types
`int`:  Int, escaped with `%d`
`float`:    Single Float, escaped with `%f`
`double`:   Double Float, escaped with `%f`
`char`:     Character, wrapped in `''`, escaped with `%c`
`char str_name[]`:  Char Array(String), should add `\0` at the end, escaped with `%s`
`char *str_name`:   String, wrapped in `""`, without adding `\0`
`char *var_name[]`: Arrays of strings
`const`:    Made a specified var a constant, make its value unmodifiable(read-only).


### For loop

    for (INITIALIZER, TEST, INCREMENT) {
        CODE
    }

INITIALIZER only run once at the beginning.  
If the current for loop VAR past the TEST, CODE run.  
After CODE ran, INCREMENT works, incresase the VAR in the for loop.  
Watch again if VAR past the TEST, if yes, continue LOOP, if not, STOP.



### Handy Tools
Error check
    http://valgrind.org/downloads/


### Details about `make`
* Make assmue there's a file called `Makefile` in current directory and run it.  
Basically you can add any shell command in the Make file. Below is an example:

    Z="zen_on_the_moon"

    fun:
        touch $Z
        now=$(shell date)
        echo "file created on"$(now) >> $Z

> In make file, you use `$(variable_name)` to get variable, and `$(bash command)` to get command execute result.

* add an `all:` item in `Makefile`, then you can use mere `make` command to to activate what's inside `all:` item.

* You can make several item(lists) at once, such as:

    make program_1 program_2


### complile a program

1. Using `make` to make an executeable file with the same name as c code file

    # assuming you have my_program.c file already
    make my_program

2. Using `cc` (clang compiler) to specify source file and target file.

    cc my_program.c -o arbitary_name_for_executable_file


### Prinf Formatters & Specifiers
[Tutorial](http://www.codingunit.com/printf-format-specifiers-format-conversions-and-formatted-output)

Formatters:

    \n  new_line
    \t  tab
    \r  carriage return
    \b  backspace
    \v  vertical tab
    \f  new page

Specifiers:
A format specifier follows this prototype:  
`%[flags][width][.precision][length]specifier`

Belowing are results from printing different format of -99, 15, 3.1415926

    specifier       Output                          Examples
    d or i      Signed decimal integer              -99
    u           Unsigned decimal integer            15
    o           Unsigned octal                      17
    x           Unsigned hexadecimal integer        f
    X           Uppercase unsigned hexadecimal      F
    f           Decimal floating point, lowercase   3.141593
    F           Decimal floating point, uppercase   3.141593
    e           Scientific notation lowercase       3.141593e+00
    E           Scientific notation uppercase       3.141593E+00
    g           min(%e, %f)                         3.14159
    G           min(%E, %F)                         3.14159
    a           hexdecimal floating, lowercase      0x1.921fb4p+1
    A           hexdecimal floating, uppercase      0X1.921FB4P+1
    c           Character
    s           String of characters
    p           Pointer address
    n           现在不知道干什么的神秘存在
    %           %% prints symbol %
