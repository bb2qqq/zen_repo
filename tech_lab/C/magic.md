### 用char表示数字0
    # 代码
    int main () {
        char nul_char = '\0';
        int my_int = 5;
        int another_int = my_int * nul_char;

        printf("nul_char: %d\n", nul_char);
        printf("another_int: %d\n", another_int);
        return 0;
    }

    # 运行结果
    nul_char: 0
    another_int: 0

### 打印字符的ascii值
在c语言里,当你声明一个变量值是int, 同时给该值赋值一个字符，系统会自动打印该字符的ascii值。

### 用汉语作为变量名

    void main () {
        char *中文变量 = "我是你爸爸";
        printf("%s\n", 中文变量);
    }

之所以能这样做是貌似新的C++标准增加了对英文字符做变量名的支持，具体是哪个版本的标准，我目前没有搞清楚。[这是我的提问](http://stackoverflow.com/questions/34526432/start-from-which-version-does-c-standard-support-non-alphanum-variable-name?)
