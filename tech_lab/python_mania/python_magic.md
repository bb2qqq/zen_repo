[//]: # (此文件里的技巧可以保证适用于python2.7版本，但在较旧或3系列的python版本里，可能会失效)
### GET absolute path of current file
    import os
    CUR_PATH = os.path.abspath(os.path.dirname(__file__))

> you can combine `CUR_PATH` with `os.path.pardir` to make a parent path of `CUR_PATH`,  
> by using `os.path.join(CUR_PATH, os.path.pardir)`.

### Return the last value if a seires a value is all True, otherwise get the first value equavilent to False
    rc = 1 and 2 and 3
    >>> rc
    3
    rc2 = 'aa' and False and 0
    >>> rc2
False

### Make a tmp file
    import tempfile
    file_descriptor, file_path = tempfile.mkstemp()


### Copy multiple object in a list

    1.  `['obj'] * 10`
    2.  `list(itertools.repeat('obj', 10))`


### Else if in single expression

**List Comprehension**

    >>> [i if i < 0 else (i, 2) if i%2 == 0 else "good" if 1 < i < 10 else 'bad' for i in range(10)]
    [(0, 2), 'bad', (2, 2), 'good', (4, 2), 'good', (6, 2), 'good', (8, 2), 'good']

**lambda function**

    complicate_lambda_func = lambda *args, **kwargs: \
        "No message" if len(args) + len(kwargs) < 2  \
        else "Yes, sir!" if ('id' in kwargs and kwargs['id'] == 'General') \
        else "There is no door for you" if 'alibaba' in args \
        else "It's already long enough, let's top here"

    >>> complicate_lambda_func(1,2,3)
    "It's already long enough, let's top here"
    >>> complicate_lambda_func(command='fuck me', id='General')
    'Yes, sir!'
    >>> complicate_lambda_func("老乡", "开门啊", "我是", 'alibaba')
    'There is no door for you'

看完上面两个例子，我越发觉得elif是源自于 `else value if conditon` 的表达方式了。  
不过与elif不同的时候，上述例子的`else if`表达式最后一定得跟一个单纯的`else`语，不然报错在等着你！


### Print without newline
If you use a comma in the end of your print statement, you will not print newline character(python2.7):

    >>> for i in range(6):
    ...     print i,
    ...
    0 1 2 3 4 5

[More discussions](http://stackoverflow.com/questions/18908897/whats-ending-comma-in-print-function-for)

### Unpacking Argument Lists
在python里你可以使用`*`来给函数定义可接受任意个参数。同时你也可以用`*`来将一个iterator unpack成一系列args传给函数!  
str, list, tuple, dict都可以使用这个技术，不过dict出来的参数顺序可能是乱的，因为hash的特性。  

    def print_args(*args):
        print " -- ".join(map(str, args))

    # Str
    >>> print_args(*"Monster")
    M -- o -- n -- s -- t -- e -- r

    # List
    >>> print_args(*range(5))
    0 -- 1 -- 2 -- 3 -- 4

    # Tuple
    >>> print_args(*("Harry Poter", "Princess White"))
    Harry Poter -- Princess White

    # Dict
    >>> print_args(*{"a":1, "b":2, "c":3, "d":4})
    a -- c -- b -- d

### Unpacking keyword args
Mapping object可以用`**`来unpacking, 但是key必须是字符串。  

    def print_kwargs(**kwargs):
        for i, j in kwargs.items():
            print i, '\t', j

    >>> print_kwargs(**{"a": 1, "b": 2})
    a   1
    b   2

你也可以自定义一个对象，只要它有`__getitem__`和`keys`两个方法并且有符合规范的处理逻辑， 它也能被`**`unpacking.  
[stackoverflow相关讨论](http://stackoverflow.com/questions/34285414/how-to-define-self-made-object-that-can-be-unpacked-by)

    class MyMapping(object):
        def __getitem__(self, key):
            if int(key) in range(5):
                return "Mapping and unpacking!"

        def keys(self):
            return map(str, range(5))

    >>> my_mapping = MyMapping()
    >>> print_kwargs(**my_mapping)

    1   Mapping and unpacking!
    0   Mapping and unpacking!
    3   Mapping and unpacking!
    2   Mapping and unpacking!
    4   Mapping and unpacking!


### 调用运算结果的属性。

在Python里，如何将一个函数名指给一个运算结果的属性？  
你只需要将运算结果用`()`包裹起来，接着便可把`()`当成一个对象，调用它的属性了！  

    from datetime import datetime
    unix_start_date = datetime.fromtimestamp(0)
    current_date = datetime.now()
    delta_date = (current_date - unix_start_date).days


### Format String with dictionray variables

    my_dict = {
        "my_name": "Liu ting",
        "my_age": 13,
        "my_boss": "Liu lao gen",
        "adjective1": "Handsome",
        "adjective2": "Dirty",
        "python_toy": (set(["Secondary life", "Love me", "You bold bold!"]), {"Idol": "DggggJ", "Hijastra": "XOK"}, ["P", "Y", "T", "H", "O", "N"]),
    }

    print "大家好，我叫{my_name}, 今年{my_age}岁，我的老板叫{my_boss}, 他有时候{adjective1},有时候{adjective2}, 我最爱的玩具是: \n\n{python_toy}".format(**my_dict)



### 对原函数/类方法进行inspect/审查的decorator

    def function_inspecter(func):
        def new_func(*args, **kwargs):
            Lucky_number = [6, 7, 8, 9]
            result = func(*args, **kwargs)
            if type(result) == int and result in Lucky_number:
                return "You are Lucky"
            else:
                return result
        return new_func


    def method_inspector(method):
        BANNED_WEBSITES = ['google', 'facebook', 'youtube', 'twitter']
        BANNED_WORDS = ['法轮功', '共产党']

        def new_method(self, *args, **kwargs):  # 此处的self参数是为了对类方法进行inspect所加
            if getattr(self, 'name', None) in BANNED_WEBSITES:
                return "404 网站无法访问"
            result = method(self, *args, **kwargs)
            for i in result:
                if type(i) != str:
                    continue
                for banned_word in BANNED_WORDS:
                    if banned_word in i:
                        return "该网站含有不恰当内容"
            return result

        return new_method


### 将任意字符串变成全局变量

      target_string = raw_input()
      command_1 = 'global %s' % target_string
      exec(command_1)
      globals()[target_string] = self


### 在全局变量中执行字符串命令
exec默认是在locals()变量环境里执行语句，如果想要在全局变量环境里执行的话

你需要使用 `exec 'my_command' in globals()`  
如果需要在本地和global的混合环境里执行命令，你使用`exec 'my_command' in globals(), locals()`  

[相关讨论](http://stackoverflow.com/questions/2083353/cannot-change-global-variables-in-a-function-through-an-exec-statement)
[官方文档](https://docs.python.org/2/reference/simple_stmts.html#the-exec-statement)


### 查看一个OBJ的代码依赖关系
    import traceback
    # inside something
    for i in traceback.extract_stack:
        print i


### 查看一个变量是否是函数
    hasattr(var, '__call__')


### 反转变量True False属性
    a = "Hi"
    a = not a
    a
    False
    a = not a
    a
    True


### 小心浮点数
在python2.7里，你指定一个值，st=0.7999999999999，你调用该值，得到0.7999999999999， 你print它， 你得到的是。。`0.8`


### 让你的程序运行指定的时长
    import signal
    import sys

    def terminate_func(*args, **params):
        # do your final things here before exit
        sys.exit(0)

    signal.signal(signal.SIGALRM, terminate_func)
    signal.alarm(100)   # after 100 seconds of running, execute terminate_func

> The running time isn't precise, like signal.alarm(100) could use 100.00013332 seconds.

### python2做除法时直接求浮点数
    >>>from __future__ import division
    >>>2/3
    0.6666666666666666
    >>>3/3
    1.0

> 在python 3中，此种除法方式是default行为

### 将url中特殊字符(% + alphanum表示的那些字符)进行转换
    import urllib
    converted_str = urllib.unquote(raw_url_str)

### 将一个大列表以n的跨度切割成若干小列表
    new_list = [raw_list[i:i+n] for i in range(0, len(raw_list), n)]

### 使用文件名字符进行from m import *操作
    agent = importlib.import_module(module_name)
    globals().update(vars(agent))

### 将一个python数据转换成json格式
    import json
    converted_json_data = json.dumps(raw_python_data)

### 让一个python文件打印自己的所有内容！
    print open(__file__).read()


### 在cent-OS上给python安装mysql模块
    # First you shall install mysql-devel, such as:
    yum install mysql-devel
    # Then install mysql module in python
    pip install mysql


### 一句话反转字典键值对
    inv_map = {v:k for k,v in my_dict.items()}

### 简单粗暴解决各类utf-8编码问题

    # coding: utf-8
    import sys
    reload(sys)
    sys.setdefaultencoding("utf-8")


### 查看当前python进程使用的内存大小
    import resource
    mem_usage = resource.getrusage(resource.RUSAGE_SELF)
    print mem_usage.ru_maxrss

    # OSX 下的单位是byte, 而Linux下的单位是kilobyte
    # 将RUSAGE_SELF 换成 RUSAGE_CHILDREN 来查看子进程的内存占用

### 判断一个对象的大小
    # 方法1
    import sys
    sys.getsizeof(object[, default])

    # 方法2
    object.__sizeof__()

### 判断一个对象是否是iterable
    if hasattr(my_obj, '__iter__')


### 获得当前文件路径
    import os
    os.path.dirname(os.ptah.abspath(__file__))      # 文件存储路径
    os.getcwd()                                     # 当前所在的执行路径

### 检测一个对象是否是字符串(包括普通字符和unicode字符)

    isinstance(obj, basestring)

### Write several statement in a line.(using ;)

    salary=1000; bonus=1200; print salary + bonus


### Log detailed error info without exit python process

    import traceback
    import sys
    try:
        eval('Your Arbitary Code here')
    except:
        print 'This is diy error log'
        print traceback.format_exc()
        print sys.exc_info()

> SyntaxError can only be caught when the code executed in eval or exec. Try remove eval and quote, you'll know what I mean.

### Convert python data structure to json

    import json
    json_data = json.dumps(my_dict)


### print ###

* To print without carriage, you add a comma after what you wanna print

    print 'my string',


### Arithmatic operation ###

* convert a string coded in base-n system into decimal number

      int(str, base_n)
      e.g: int('0xAE', 16)



## DATA STRUCTURE ##


#### SET OPERATION ####

    UNION               s | t           #  all elements in s and t, except duplicate
    INTERSECTION        s & t           #  elements that are in s and t
    DIFERENCE           s - t           #  element in s but not in t
    SYMMETRIC_DIFFER    s ^ t           #  equal to (s - t) | (t - s), means that element in t or s that are not appeared in both set




## DATETIME AND TIME

### 获取当前某个日期午夜的datetime对象
    # 假定我们拿到了传入的datetime_obj
    from datetime import datetime
    mid_night = datetime.combine(datetime_obj.date(), datetime.min.time())

    # 一个判断传入字符串是否是当日零点的函数
    def is_midnight(date_str, date_format="%Y-%m-%d %H:%M:%S"):
        """检查字符串是否是当日的午夜。"""
        datetime_obj = datetime.strptime(date_str, date_format)
        datetime_midnight = datetime.combine(datetime_obj.date(), datetime.min.time())
        return datetime_obj == datetime_midnight


### 获取当前自然日的日期字符串

    from datetime import datetime
    natural_date = str(datetime.now().date())

### Formate Year/Month/Day without 0 padding

        import datetime
        "{dt.year}{dt.month}{dt.day}".format(dt=datetime.datetime.now())

>   This will delete the key-value pair if key in my_dict, otherwise defualt_value will be returned, so you won't get an error when key isn't in my_dict

### 快速将字符串解析成datetime对象
    from dateutil import parser
    datetime_obj = parser.parse(datetime_str, fuzzy=True)

> fuzzy=True会开启模糊模式，忽略一些parser不能识别的字符

### 快速打印格式化的当前年月日和时分秒
    import time
    time.strftime('%F %T')
    # %F 是年月日在time模块里的快捷表示，%T是时分秒的快捷表示, 样例：2015-01-01 00:00:00



* if List_A exists, iter over List_A, otherwise iter over List_B

        for i in List_A or List_B:
            print i


* delete one item from a dict

        my_dict.pop(key, default_value)
