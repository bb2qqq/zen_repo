### 在OSX下用sed替换大量文件里的关键词

    sed -i "" 's/old_word/new_word/' target_files

### 批量修改代码

如下的代码，会找到所有调用某特定方法(getMembers)所获得的变量，判断该变量的值，如果满足预设条件（0），则返回特定值（0)

    # Linux 版本(Using `gsed` on OSX)
    gsed "s/\([\t ]*\)\([A-Za-z0-9_]*\).*getMembers.*/&\n\1if \2 == 0: return 0/"


### Find line contains keyword and del it

      sed -i '/key_word/d' target_file


### Print specific line(Linux)
Here print the line 100

      sed -n '100p'

### Using diy separators

In sed, you can use arbitrary character as separator,  
as long as it was not a Regex Symbol or in the substitue pattern.  
Remember there are totally 3 separators.  
Please check the examples below.

    # Using F as separator
    => echo "Huge" | sed sFHFMF
    Muge

> But for better reading experience, you'd better choose a character which can distinguish patterns well.



### [待整理博客日志](http://zenofpython.blog.163.com/blog/static/235317054201452242843555/)

    测试后我发现，上面的命令只能将mamamia中的mama替换一次。也就是说每行只能替换一次。
    原来sed里的separator是可以自定义的，只要他不在你要换的符号里或是某种正则表达符号就行，理论上。记得有三个分隔号哦~ 我们来试试：
    $ echo "mama mia" sed sb"mama""Papa"
    Wow, that's cool.
    另外，如果你想给你找到的Pattern加上一些符号，你可以用 &来指代之前的pattern, 如：
    $ echo "mama mia""mama""*& ->&<- ^&^"

    Super cool. Love sed now.
    一个小技巧，如果你需要将一个长的match pattern删掉许多不要的部分，你可以用()和\1的正则表达法。sed最多可以记忆9个() part.   妈的，写的例子竟然不好用，待正则表达式功力更强再来填这个坑  【待补充】
    ----------------------------------------------------------------------------------------------------------------------------------------
    在separator后可以加各种flag。比如 g 意味着 global replacement, 之前我们一行只能换一个词的问题可以通过它来解决
    $ echo "mama mia" sed sx

    papa pia 
    如果有一行内有多个满足pattern的内容，你只想更换其中指定的第某个，你在最后一个分隔号前加上相应的数字就行了：
    $ echo "mama mia"

    mapa mia
    如果数字和g - flag结合的话，表明从第n个pattern开始，替换该pattern及其后的所有pattern，如：
    $ echo "mama mia"

    mapa pia
    * 数字flag的范围是1-512
    当你想一次执行多个sed命令时，你在sed后每个命令前加上 -e 的选项，如：
    $ echo "mama mia"

    popo pio
    同awk一样，sed也可以直接作用于文件
    "suck""puck""dick""nick"

    helloworld
    -n option 表示静默，不print任何信息，除非在命令尾部发现 /p 。可以用来只打印特征行。嗯，用来筛选特征项后再用sort排序，不错。试一下：
    "suck""*uck""dick""*ick"p test
    sed不用s替换也可以用来检查pattern, 你使用 sed /pattern/address的模式
    p test
    -i option可以修改原文件，这样免去了写入新文件再mv回去的麻烦
    注意！ 如果你试图像我之前一样，用如下命令
    $ sed s
    你的file将变成空白，原理请看这儿
    * 在OS X下需要在-i 后面传个参数作为备份，如果传0的话
    -------------------------------------------------------------------------------------------------------------
    要替换整行，你需要用到c命令，请看：
    cpikapika

    pikapika
    系统可以自动检测到 / 后面的c,  当然，为了增强可读性，在其后面加个backslash会是个好主意：
    c\pikapika
    --------------------------------------------------------------------------------------------------------------
    同awk一样，sed 的 -f 也是用来执行script. 不过sed script 看起来真的有点简陋啊
    如果命令太长，你也可以使用\ 来换行，不过和python里一样，小心它后面跟着的空格巫师！~
    如果你用的是bash，有个更简单的方法将长命令换行，直接用单引号把它们括起来：
    s/a/B/g

    s/b/C/g

    s/c/D/g'
    要替换指定行里的内容，在用单引号括起来的s系列命令前加行号就行：
    '3 s/o/*/g'

    helloworld
    上述code里的3可以替换成任意正则表达式，正则表达式的expression你用/ / 括起来, 记得用' '括起来表达式和s命令哦：
    '/k$/ s/o/@@@/'

    helloworld
    m@@@ck 
    *上述的行号限制和正则表达式与s命令间的空格都不是强制添加的，加上是为了增强可读性
    * 注意，如果你在sed里读取两个文件的话，读取第二个文件时，行号不会清零，而是从第一个文件尾部行号开始累加
    -------------------------------------------------------------------------------------------------------------------
    要搜索从某一行到另一行间的内容，在两个行号间加个 逗号（，）就行，试看：
    '3,5 s/a/&/p'

    Simple  better than complex
    Complex better than complicated
     better than nested
    要替换某行到最后一行的内容，将第二个行号换成 $ 即可。
    -------------------------------------------------------------------------------------------------------------------
    d表示删除, 如下命令删除了zen文件中的2到18行，并将结果打印出来：
    '2,19 d'

    Beautiful  better than ugly
    -------------------------------------------------------------------------------------------------------------------
    如果要反向搜索（搜索不匹配的），你有两种方法，!p 表示打印不匹配的行
    '/k/ !p'

    helloworld
    或者是：
    '/p/ d'

    helloworld
    --------------------------------------------------------------------------------------------------------------------
    q 可以中断sed的编写，一般用于条件控制。下例是一个简单的 q 命令用法：
    Beautiful  better than ugly
    Explicit better than implicit
    Simple better than complex
    --------------------------------------------------------------------------------------------------------------------
    之前我们说过可以用-e, 或者'  '包裹来执行长命令，而你还能用{ } 来执行 nested 的命令
    '5,15 {

              /purity/,/ambiguity/ {

              s/a/A/g

    Beautiful better than ugly
    Explicit better than implicit
    Simple better than complex
    Complex better than complicated
     better than nested
    Sparse better than dense
    Readability counts
    Special cases aren't special enough to break the rules.
    Although prActicAlity beAts purity.
    Errors should never pAss silently.
    Unless explicitly silenced.
    In the fAce of Ambiguity, refuse the temptAtion to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you'Dutch
     better than never
    Although never  often better than right
     the implementation  hard to explain's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let' more of those
    其实，你把这个命令平铺了写效果是一样的。sed tutorial的作者说展开写好看，方便扩展。
    '5,15 {/purity/, /ambiguity/ { s/a/A/g} }'
    * 注意，如果文本内容里有两个/purity/ pattern, 替换将启用两次，直到sed再次遇到第二个/ambiguity/才会停止。上述代码里原来用的是 /Although/ 和 /There/ 作为起始pattern, 结果第二个Although后面也把a变成了A . 目前为止我还没有找到解决办法，所以或许选一个好的/start/ 和 /stop/ pattern是一个权宜之计。
    -----------------------------------------------------------------------------------------------------------------------
    w命令可以用来写入文件，虽然我觉得它和输出导向符有冲突，简单一例：
    '/hello/ w toy'

    cat toy

    helloworld
    ----------------------------------------------------------------------------------------------------------------------
    r 可以读取一个file，并且把它的内容 print 在按/pattern/ 匹配的当前文件中，如
    '$ r test' test2

    skirt
    pussy

    helloworld
    如同我们提过的， $表示末尾， 这儿它是文件的尾行。
    同样的，你可以使用正则pattern:
    '/mo/ r test2'

    helloworld

    skirt
    pussy
    -----------------------------------------------------------------------------------------------------------------------
    使用 a  命令，你可以轻易地按pattern append line. 它会将你指定的内容加在pattern line后。 如：
    '1 a "wanna explore"' test2

    skirt
    "wanna explore"
    pussy
    或者：
    '/pus/ a "taste salty"' test2

    skirt
    pussy
    "taste salty"
    i 命令和 a 命令类似，不同的是，它把行加在pattern line之前。
    '1 i "A hot girl is wearing"' test2

    "A hot girl is wearing"
    skirt
    pussy
    之前我们提到了 c 命令可以替换整行，这儿我们再来复习一下
    '1,3 c "Purged, you satisfied? Mr. clergy."' test2

    "Purged, you satisfied? Mr. clergy."
    叮咚！这儿我们把1到3行全换成了一行。要怎么一行行换呢？
    经过stackoverflow 和 google后，我发现了如下方法：
    '1,3 s/.*/"Lady, could you borrow me your ass for a while? I am in hurry"/' test2

    "Lady, could you borrow me your ass for a while? I am in hurry"
    "Lady, could you borrow me your ass for a while? I am in hurry"
    "Lady, could you borrow me your ass for a while? I am in hurry"
    " .  "在正则表达式里表示任意符号， * 表示它之前的符号匹配0次或任意次。所以在上述代码里我们先搜索行号，再把其中每一行所有内容替换成我们想要的内容。
    -----------------------------------------------------------------------------------------------------------------------------
    如果你想要逃脱单引号 ' , 请不要用一对单引号' '将表达式包起来，如：
    's/.*/\'/'# 错误！！！会导致sed解析错误，出现下面的延长输入提示符 >
    这样做可以达到你的目的：
    $ sed s
    --------------------------------------------------------------------------------------------------------------------------------
    在sed里，你可以用 = 来打印行号，如果你想在一个/begin/, /stop/ parttern里来打印行号的话，你需要用{ } 将 = 括起来，因为 = 在sed中原本是只能接受一个address的， 我们需要用花括号来帮助它指定作用域，也就是花括号外部定义的pattern.
    先看简单一例:
    再看pattern搜索的例子:
    '/mock/,/no/ {=}'
    Easy, huh? 
    注意，用=号打出来的行号和原文本不是在同一行的哦，而是在原文本的上面一行，试看：
    helloworld
    ---------------------------------------------------------------------------------------------------------------------
    在sed tutorial里，作者说可以使用y来更换大小写， 如：
    'y/abcdef/ABCDEF/'

    hElloworlD
    研究后发现 y 命令是一次将多个字符依次地替换成后面的字符，前后两个分隔符的字符数必须相同，试看：
    'y/abcdef/MNBVCX/'

    hClloworlV
    # extra research start #
    好奇去stackoverflow上搜了搜，发现了一些其他的实现方法，以及一个新工具 tr
    1. 用sed内置正则加s:
    's:\(.*\):\U\1:' tee TEST

    HELLOWORLD
    MOCK MY DICK
    NO STOP
    聪明的你一定发现了，上文的 \U 代表了通通转成大写，那么不难推测，\L可以通通转成小写:
    's:\(.*\):\L\1:'

    helloworld
    awk有一个tolower的方法来将文本变成小写，与之对应的是toupper方法
    '{print toupper($0)}'

    HELLOWORLD
    MOCK MY DICK
    NO STOP
    $ echo I\'m BIG BOSS '{print tolower($0)}'

    'm big boss
    新发现的工具tr转换的方式如下，其特性楼主尚未完全掌握：
    HELLOWORLD
    MOCK MY DICK
    NO STOP
    -----------------------------------------------------------------------------------------------------------
    sed tutorial里有关于读取多行的技巧，目前感觉还不需要用到，如果你需要的话，你会用到 N 命令【待续】
