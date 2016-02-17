此模块提供除python常规data-type外的container(High-performance)，同时给用户自定义container提供了一些工具

### 带名字的tuple

Defining of `namedtuple`: `namedtuple(typename, field_names, verbose=False, rename=False)`
If verbose is True, the definition of who class will be printed.  
If rename is True, invaild fields name will be replaced with positional names.  
For example, `['abc', 'def', 'ghi', 'abc']` is converted to `['abc', '_1', 'ghi', '_3']`, eliminating the keyword def and the duplicate fieldname abc  
You can use it to produce a named tuple Class:

    FootballPlayer = namedtuple("football_player", ("skill", "strength", "speed", "cooperation"))
    suarez = FootballPlayer(skill=8, strength=8, speed=8, cooperation=8)
    iniesta = FootballPlayer(skill=10, strength=7, speed=7, cooperation=9)
    messi = FootballPlayer(skill=10, strength=8, speed=7, cooperation=9)
    neymar = FootballPlayer(skill=10, strength=7, speed=8, cooperation=8)
    busquets = FootballPlayer(10, 9, 7, 10)

    >>> max([messi, neymar, iniesta], key=sum)
    football_player(skill=10, strength=8, speed=7, cooperation=9)
    >>> max([neymar, messi, iniesta, busquets], key=lambda x: x.strength)
    football_player(skill=10, strength=9, speed=7, cooperation=10)

    >>> messi.skill
    10
    >>> neymar[3]
    8
    >>> iniesta_attrdict = iniesta._asdict()   # convert to dict
    >>> iniesta_attrdict['speed']
    7
    >>> new_busquets = busquets._replace(cooperation=100, skill=200)
    >>> new_busquets
    football_player(skill=200, strength=9, speed=7, cooperation=100)

### deque, 一个可在两端快速append和pop数据的list-like container

deque是"double-ended queues"的缩写，发音与`deck`相仿。  
定义：class deque([iterable[, maxlen]])

如果iterable为空或未输入，返回一个空的deque对象，  
如果maxlen被定义，当deque长度达到maxlen，在一端append数据，会导致另一端的相应数据被抛弃掉。  

deque支持如下方法：

    # 与list相仿的方法
    count(x)
    append(x)
    extend(iterable)
    pop()
    remove(value)
    reverse()


    extendleft(iterable)
        将iterable里的item一个个从左端加入，最后的表现形式像是把iterable的顺序reverse了。

    appendleft(x)
        将x加到deque左端

    clear()
        清除deque中所有元素

    popleft()
        从deque左端去掉一个item并返回它。

    rotate(n)
        将deque里每一个元素向右移动n步，如果n是负数，向左移动n步。元素 + 移动步数超过deque长度后会从deque左端开始继续移动

deque可以用来很方便的实现`moving average`, 这是统计学上一种重要的分析方法，股价里的K线就是运用了这种技术，它也被考虑为卷积。下面是实现方法：

    def moving_average(iterable, n=3):
        # moving_average([40, 30, 50, 46, 39, 44]) --> 40.0 42.0 45.0 43.0
        # http://en.wikipedia.org/wiki/Moving_average
        it = iter(iterable)
        d =  deque(itertools.islice(it, n-1))
        d.appendleft(0)
        s = sum(d)
        for elem in it:
            s += elem - d.popleft()
            d.append(elem)
            yield s / float(n)
