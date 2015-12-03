""" This tutorial is based on python 2.7"""
[Python 2 Source Code](https://www.python.org/downloads/release/python-2710/) [//]: # (选Gzipped source tarball)  
[Python 3 Source Code](https://www.python.org/downloads/release/python-350/) [//]: # (选Gzipped source tarball)  
[PYPY Source Code](https://bitbucket.org/pypy/pypy/downloads) [//]: # (选Download repository)

## Descriptors                                                                                                                          <a id="Descriptors"></a>

### Definition and Introduction
In general, a descriptor is an object attribute with "binding behaviour", one whose attribute access has been overriden by methods in the descriptor protocol.  
`__get__()`, `__set__()` or `__delete__()` forms the descriptor protocol.  
If any of these three methods are defined for an object, the object is said to be a descriptor.  

The default behavior for attribute access is to get, set, or delete the attribute from object's dictionar y.  
For instance, `a.x` has a lookup chain starting with `a.__dict__['x']`, then `type(a).__dict__['x']`, and continuing through the base classes of type(a) excluding metaclasses. [Metaclass Introduction][MI]  
If the looked-up value is an object in whinch defined one of the descriptor methods, then Python may override the default behavior and invoke the descriptor instead(if it is a data-descriptor and `__getattribute__` not overriden).  
Descriptors only work for new style objects and classes. (classes which inherits from `object` or `type`)  

Descriptors are generally used. They are mechanism behind properties, methods, static methods, class methods, and super().  
They are used throughout Python itself to implement the new style classes. Descriptors simplify the underlying C-code and offer a flexible set of new tools for everyday Python programs.

### Descriptor Protocol

`descriptor.__get__(self, obj, type=None) --> value`  
`descriptor.__set__(self, obj, value) --> None`  
`descriptor.__delete__(self, obj) --> None`  

`non-data descriptors` are those with only `__get__` method, meanwhile `data descriptors` does have both `__get__` and `__set__` method.  
`data descriptors` precede instance's dictionary, meanwhile `non-data descriptors` has lower priority than instance's dictionary.  

If you want to make a read-only `data descriptor`, you can defining its`__set__()` method like this:

      def __set__(self, obj, value):
          raise AttributeError("This is a read-only data-descriptor!")

### Invoking Descriptors

You can call `descriptor.__get__(obj)` directly. Or you can trigger it upon attribute access(`object.my_attr`).

For objects, the machinery is in `object.__getattribute__()` which transforms `b.x` into `type(b).__dict__['x'].__get__(b, type(b))`.  
For classes, the machinery is in `type.__getattribute__()` which transforms `B.x` into `B.__dict__['x'].__get__(None, B)`. In pure Python, it looks like:

      def __getattribute__(self, key):
          "Emulate type_getattro() in Objects/typeobject.c"
          v = object.__getattribute__(self, key)
          if hasattr(v, '__get__'):
              return v.__get__(None, self)
          return v

The important points to remember are:

      * descriptors are invoked by the __getattribute__() method
      * overriding __getattribute__() prevents automatic descriptor calls
      * __getattribute__() is only available with new style claesses and objects
      * object.__getattribute__() and type.__getattribute__() make different calls to __get__().
      * data descriptors always override instance dictionaries.
      * non-data descriptors may be overridden by instance dictionaries.

The object returned by `super()` also has a custom `__getattribute__()` method for invoking descriptors. The action `super(B, obj).m` searches `obj.__class__.__mro__` for the base class `A` immediately following `B` and then returns `A.__dict__['m'].__get__(obj, B)`

### Properties
Calling property() is a succint way of building a data descriptor that triggers function calls upon acess to an attribute. Its signature is:

property(fget=None, fset=None, fdel=None, doc=None) -> property attribute

Below is a pure Python version of Property Mechanism:

    class Property(object):
        "Emulate PyProperty_Type() in Objects/descrobject.c"

        def __init__(self, fget=None, fset=None, fdel=None, doc=None):
            self.fget = fget
            self.fset = fset
            self.fdel = fdel
            if doc is None and fget is not None:
                doc = fget.__doc__
            self.__doc__ = doc

        def __get__(self, obj, objtype=None):
            if obj is None:
                return self
            if self.fget is None:
                raise AttributeError("unreadable attribute")
            return self.fget(obj)

        def __set__(self, obj, value):
            if self.fset is None:
                raise AttributeError("can't set attribute")
            self.fset(obj, value)

        def __delete__(self, obj):
            if self.fdel is None:
                raise AttributeError("can't delete attribute")
            self.fdel(obj)

        def getter(self, fget):
            return type(self)(fget, self.fset, self.fdel, self.__doc__)

        def setter(self, fset):
            return type(self)(self.fget, fset, self.fdel, self.__doc__)

        def deleter(self, fdel):
            return type(self)(self.fget, self.fset, fdel, self.__doc__)

property**机理描述**：
当你使用property()的时候，你实际上获得了Property类的一个实例。Property类在自己的`__get__, __set__, __delete__` descriptor methods里嵌入了`fget, fset, fdel`的逻辑，并用它们来完成相应的`get, set, delete`操作。而你，通过向`property()`传入自定义的`fget[, fset, fdel]`方法，来获得一个间接的自定义descriptor的实例。此外，Property类还提供了`getter, setter, deleter`方法，供property实例使用。它们的作用机理见如下范例：

    class Sample(object):
        self._val = 153

        # 我们申请了一个名字"height", 把它的函数主体作为fget参数传给property()
        # property根据此参数， 生成了一个Property的实例
        # Sample把"height"作为key放进自己的`__dict__`里，把上一步生成的Property实例作为相对应的value,
        # 其代码描述是 Sample.__dict__["height"] = Property(fget=height_func_body)
        # 当我们用Sample类生成一个实例sample，并使用sample.height语句时，根据descriptor机理，在一系列中间过程后，
        # 我们会去获得type(sample).__dict__('height').__get__(sample, type(sample))的值。
        # 所以实际上，我们这儿在调用Property(fget=height_func_body).__get__(sample, type(sample))方法
        # 我们再去看Property类里的__get__方法，会发现它在边际条件判断后，返回self.fget(sample)的值
        # 而对于该Property实例而言此处的 fget 就是 height_func_body(一个函数处理逻辑，没有函数名) ，它接受一个参数，并返回该参数的_val属性。
        # 所以此处，我们会返回sample._val，该实例并没有_val属性，所以返回type(sample).__dict__['_val']的值，也就是153
        #
        # PS: height_func_body 是指如下代码逻辑，
        # def ____(arg):       # ____ 用来代替height, 因为height最后指向的实际是@property处理完后的Property实例, 但____也不是此body的函数名，此body有过临时构建函数名，但被消灭了
        #     return arg._val

        @property
        def height(self):
            return self._val



        # 我们在这儿用的decorator是height.setter，也就是说我们会把此处的function_body传给height.setter，
        # 把获得的返回值挂载在function_name，也就是"height"上，挂载方式是Sample.__dict__[function_name] = decorate_result
        # 此处decorator里的height，实际上是我们之前用@property获得的Property实例。
        # Property实例的setter方法是如何运作的呢？我们可以看到他定义了两个传入参数self, 和fset.
        # 当我们在Property实例里调用此方法时，第一个参数self实际上被指向了这个Property实例自身。
        # setter的逻辑语句只有一行： return type(self)(self.fget, fset, self.fdel, self.__doc__)
        # type(self)得到的是Property类，向Property类传入self.fget, fset, self.fdel, self.__doc__ 等参数，我们会得到什么呢？
        # Bingo, 一个新Property实例出现了。
        # 这个新的Property实例拥有原来的Property实例的`fget, fdel, 和 __doc__`属性，同时将`fset`属性替换为此处传向setter的function_body
        # 根据Decorator的原理，这个新实例的变量名是"height", "height"还是那个"height"只不过它指示的对象已经发生了变化。
        # 用一个比喻来形容这个过程就是： 张三被克隆了，给克隆体换了一个器官，把原有的张三消灭，管这个新的克隆体叫张三。
        #
        # PS: 从理论上讲，如果之前的Property实例被修改了除`fget, fset, fdel, __doc__`以外的属性，
        # 新获得的Property实例在使用效果上和老实例不是完全等价的。
        # 但我自己做了下实验，发现property实例对attribute修改做了保护，禁止了直接赋值。
        # 这样可以确保用`getter, setter, deleter`获得的新实例能尽可能地和原实例保持特性一致(因为有方法替换，特性肯定不会完全相同)。
        # 如果您找到了在Property实例生成后直接修改其属性的方法，请与我电邮联系: juchen.zeng@gmail.com

        @height.setter
        def height(self, val):
            self._val = val


如想进一步了解为何上文的`height_func_body`没有特定函数名，请参见相关的[Decorator文档](#Decorators)

__Important points about property__

* what property() returns is definitely a `data descriptor`, as it has default `__set__` and `__get__` method.


[How @property works?](http://stackoverflow.com/questions/17330160/how-does-the-property-decorator-work)

[MI]: http://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python

> For experiments about `non-data descriptors`, see [here](http://www.cafepy.com/article/python_attributes_and_methods/ch01s04.html)  
> 关于object里的`__getattribute__`如何运行，可以查看`~/source_code/PYPY_source_code/pypy/objspace/descroperation.py`里第80行`Object`类的`descr__getattribute__`方法。


## Decorators                                                                                                                               <a id="Decorators"></a>
### what is decorator?

It is a Syntax-Sugar in order to make function/method wrap process more readable.
Decorators looks like this:

    @dec2
    @dec1
    def my_func(*args):
        pass

when you want to use `my_func`, you are actually get the result of `dec2(dec1(func))`.  

### how to use decorator?
So, first you should make sure your decorators definition runs before your own function runs.  
And, then be aware that the decorators were executed starts from the one which is closest to `def` statement.  
Finally you should make sure **after all the decorate processes, you should get something callable**

### decorator features
* When you using decorators, you are actually saying:  
OK, I got a *var_name*, its now refers to a callable object.  
Now I'm going to pass it as an argument to a function.   
It then will pass the result of it to next function. Until the end of the decorators.  
And I will now assign the final result to *var_name*, now matter whatever it is only if it's callable.  

This means, you should take a look of what the decorators do to findout the final result.  
e.g.
    def evil_decorator(_input):
        return curse

    def curse(name):
        print "Fuck you! " + name

    @evil_decorator
    def greetings(name):
        print "Hello! " + name

Guess what will you got when you use `greetings("Mr. White")`?  
* All these processes above runs on the function definition parse-build period.  
That is to say, the decorators will run when the function code is imported/parsed, it won't wait until you call the function.  

* Another thing, you may specified serveral parameters in your original defination, but the final obj which the original name refers to,  
may take 0 parameters, or a bunch of parameters, amazing, isn't it? It all depends on what decorators give back to you.  

* During the decorating process, the original function can only be called with its obj, not with its name.  

     # Called with name, FAILED.
     # RESULT:  "NameError: global name 'print_2' is not defined"
    def switch(func):
        return print_2

    @switch
    def print_2():
        return 2

 
     # Called with obj,
     # RESULT: "2, returned the obj of print_2 funciton"
    def switch(func):
        func()
        return func

    @switch
    def print_2():
        return 2

This is to say, the name assiging is the last step of a decorating process.


* What if I called the original function in decorators, will it be an infinite loop? The answer is no.  
Only the original function will be triggered, but not the result of all decorate processes.


### decorate maker
The `@` can takes expressions after it, as it the value returned by expression is a func.  
This means you can even use eval after it.  
Here is a long expression decorator using eval:

    def ev(func):
    result = func(555)
    return result

    @eval("[i for i in globals().values() if hasattr(i, '__name__') and i.__name__ == 'ev'][0]")
    def my_print(n):
        def print_n():
            print n
        return print_n


## Bitwise operators
A bitwise operation operates on one or more bit patterns or binary numerals

* ~ (NOT) will reverse 1-0 for a number(if signed int, reverse its sign), `~7` means `reverse +0111`,  
thus we got `-1000`, which is `-8`.

    >>> ~7
    -8

* & (AND) will take two binary numbers, compare every bits of them,  
on each position, only when both number has value 1 on it, set that position to 1, else 0.  
For example. take 5(binary: 101) AND 11(binary: 1011), what we got will be `binary 0001`, that is 1.

    >>> 5 & 11
    1

If you'd like only keep last N bit of a int number, you can use `Bitwise AND` operator to do that:

    def get_last_n_bit(target_number, n):
        filter_number = int("1"*n, 2)
        return filter_number & target_number


* | (OR) is similar to &(And), but it will return 1 for each position if more than one number have value 1 on that position.  
Thus 5(b: 101) OR 11(b: 1011) should be (b: 1111), that is 15.

    >>> 5 | 11
    15

* ^ (XOR) is similar to |(OR), but it returns 1, only when exactly one number has value 1 on that position.  
If two numbers have value 1 on same position will return 0 for that position.  
Thus 5(b: 101) XOR 11(b: 1011) should be (b: 1110), that is 14.  

    >>> 5 ^ 11
    14

For its interesting character, we can use XOR to toggle switch status. Below is a toggleing code.  
    i = 0
    for n in range(6):
        i = i ^ 1
        print i
    1
    0
    1
    0
    1
    0

* >> (RIGHT SHIFT) will shift every bits of a number to right by specified steps, thus we can shrink it.  
If the step exceed max digit positions of that number, the number will be zero.  
e.g. for number 5(b: 101), if we `>>` it by 1, we got `0b10`(2), `>>` it by 2, we got `0b1`(1), etc.

    >>> 5 >> 0
    5
    >>> 5 >> 1
    2
    >>> 5 >> 2
    1
    >>> 5 >> 3
    0
    >>> 5 >> 4
    0

* << (LEFT SHIFT) is similar to RIGHT SHIFT, but on different direction, thus it enlarge the number.  
For 2(b:10), we excpet `2 << 1` to be `b: 100`, which is 4.  
We can inspect an interesting phenonemon, it seems to `<<` a number by `n` steps means to mulitply that number with `2**n`.  
Let's test it:

    def multiply_with_2_powers_n(target_number, n):
        return target_number << n

    for i in range(100):
        for j in range(20):
            assert multiply_with_2_powers_n(i, j) == i * (2**j)

     # TEST PASSED, NO ASSERTION ERROR ARISED

# Built-in Functions
### type
You can use type with 1 or 3 arguments.  
With `type(one_arg)`, you got the type of `one_arg`.  
If `one_arg` is an instance, you will get the class of that instance.  
But when you want to check the type of object, it's recommended to use `isintance(obj, type)`  

With three args form `type(name, bases, dict)`, a new type object is returned.  
TYPE REQUIREMENTS: name -> str, bases -> tuple, dict -> dict.  
This is way of dynamically define a class.  
The `name` argument is the name of class and become `__name__` attribute.  
The `bases` tuple will itemizes the base classes and become the `__bases__` attribute of the class, it will record the class's ancestors.  
The `dict` argument will initiliaze the `__dict__` attribute and update its content into it.  

Belowing are two identical ways of create a class.

    # First way
    class X(ob


    # Second way

### super
The basic usage is `super(Class, instance)`, when you use it, the following steps will happen:

1. Python check if isinstance(instance, Class) is True.
2. Python find the __class__ attribute of instance, get the the instance.__class__'s __mro__ attribute.
3. Python find the index of Class you passed to super in the __mro__ tuple in step2.
4. Python add the index of step3 by 1, use it to get the corresponding class in __mro__ tuple of step 2, and return the super delegate of this corresponding class.
5. If the index in step4 exceed length of __mro__ of step2, the delegate of last class in __mro__ of step2 is returned, which is the object class.

Below is the official doc version about `super(Class, instance)`'s behaviour:

     The call super(B, obj).m() searches obj.__class__.__mro__ for the base class A immediately following B
     and then returns A.__dict__['m'].__get__(obj, B). If not a descriptor, m is returned unchanged.
     If not in the dictionary, m reverts to a search using object.__getattribute__().




When you used `super(Class1, Class2)`, you will get the delegate whose position is after `Class1` in `Class2`'s `__mro__` list.  
And then you can use the use the delegate to call the according class methods.  


> [Discussions about how super interacts with `__mro__`](http://stackoverflow.com/questions/33890918/how-does-super-interacts-with-a-classs-mro-attribute-in-multiple-inheri)  
> [Single argument on super](http://stackoverflow.com/questions/30190185/how-can-i-use-super-with-one-argument-in-python)  

### dir
When called without arguments, return a list of names of current scope.  
If you passed an object to it, it will return a list of names of the attributes of the object.


### `eval` and `exec`

1. `eval` returns the value of expression, `exec` returns `None`.

2. `eval` only accepts single expression, `exec` has no limit.

when the input is `str`, both `eval` and `exec` will use `compile` function to compile it into bytecode first.  
The difference is they'll pass different `mode` arguemnts to `compile`,  
`eval` passes `"eval"`, `exec` passes `"exec"`, and this made up the two different features we listed above.

[Furthur Discussions](http://stackoverflow.com/questions/2220699/whats-the-difference-between-eval-exec-and-compile-in-python)


### raw\_input()

convert anything typed-in into string

    >>>raw_input()
    >>>test \n \t
    >>>'test \\n \\t'

### input()
Equal to `eval(raw_input())`

    >>>input()
    >>>1 + 1
    >>>2

### pow(a, b)
Equal to a ** b

    >>>pow(2, 3)
    >>>8



# Built-in Modules

## array

In python, an array is like a list, except it only accept certain types of value.

    >>>import array
    >>>num_array = array.array('i', range(5))
    >>>print num_array
    >>>array('i', [0, 1, 2, 3, 4])

## math

### Ceiling a number
Return value is float

    >>>import math
    >>>math.ceil(10.000001)
    >>>11.0
    >>>math.ceil(1)
    >>>1.0

### Floor a number
Return value is float

    >>>import math
    >>>math.floor(9.999999)
    >>>9.0
    >>>math.floor(8)
    >>>8.0

### Get the Square root of a number
Return value is float

    >>>import math
    >>>math.sqrt(9)
    >>>3.0
    >>>math.sqrt(3)
    >>>1.7320508075688772


## cmath
cmath refers to complicate math

### Get the Square root of a negative number
Return value is complicate number

    >>>import cmath
    >>>a = cmath.sqrt(-1)
    >>>a
    1j
    >>>a ** a
    (0.20787957635076193+0j)


## __future__
A module to store features that will be implement in future python.



# Syntaxs
### What is AST?
AST is short ofr `Abstract Syntax Tree`.  
It is a tree representation of the abstract syntax structure of a piece of source code.  
Below is a piece of pseudo-code and its AST:

    # CODE
    while b ≠ 0
        if a > b
            a := a − b
        else
            b := b − a
    return a

AST:
![](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Abstract_syntax_tree_for_Euclidean_algorithm.svg/800px-Abstract_syntax_tree_for_Euclidean_algorithm.svg.png)

> [Wiki](https://en.wikipedia.org/wiki/Abstract_syntax_tree)

### Differences between expressions and statement

1. Statemens are anything that can make up a line(or several lines) of python code.

2. Expressions is a subset of statements, it has these features:
    * Produce at least 1 value, the value can be any Python object.
    * Only contain identifiers, literals and operators.
    * Operators include arithmetic and boolean operators, the function call operator () the subscription operator [] and similar,

[Furthur Discussions](http://stackoverflow.com/questions/4728073/what-is-the-difference-between-an-expression-and-a-statement-in-python)

### if condition in 1 line
    >>>if "I'm your daddy": print "I'm your daddy"



# DATA TYPES

## String


## Number

### Hexadecimals
Hexadecimals starts with `0x`

    >>>print 0xB
    11

### Octals
Octals starts with arbitary numbers of `0`

    >>>print 011
    9

    >>>0111 == 0000111
    True

### Hash Object
hashlib.md5('target\_txt') will return a hash object with md5 algorithm.

Which stores its value as a 128-bit hash value (binary - data), and other attributes for manipulating this data.

Let's say `hash_sample` is a hash object with md5 algorithm.

Hash_sample.hexdigest() will transfer the binary into a 32 byte hex string.  
Two byte([0-9a-f]) for per 8 bit number(`max to 16*16`).  
(128/8) * 2 = 32

`hash_sample.digest()` will transfer the object's binary data into a 16 byte string:  
By default python tries to interpret the bytes as ascii using the \xhh escape to output the hex representation of any bytes not in the range of ascii.  
If there isn't such code in ascii, you'll saw unrecongnizable code on your screen when trying to print it out.  


> md5 will map the given text to a number between 0 to `2 ** 128`
