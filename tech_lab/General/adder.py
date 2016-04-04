#! coding: utf-8

# 加法器，就是计算器CPU里用来进行加法运算的那货
# 一个全加器接受加值A，被加值B和进位输入值C_in
# 输出该位结果值S, 和进位输出值C_out
# A和B很容易理解，我们要进行加法操作的对象。
# 而C_in实际上是上一个加法器计算完毕后传过来的进位值。
# 等等，为什么说上一个加法器？
# 因为，我们需要把加法器联结起来以进行多位计算。总不能只能计算1+1和0+1对不对。
# 然后C_out，就是我们告诉下一个加法器的进位值了。
# 本位结果值的计算公式是S = A xor B xor C_in
# C_out的计算公式是 (A and B) + (C_in and (A xor B))

def adder(A, B, C_in):
    S = (A != B) != C_in
    C_out = (A and B) + (C_in and (A != B))
    if S:
        S = 1
    else:
        S = 0
    if C_out:
        C_out = 1
    else:
        C_out = 0
    return S, C_out

def arbitrary_length_adder(num1, num2):
    greater_num = bin(max(num1, num2))[2:]  # bin返回的是'0b1'的格式，需去除前面的0b
    smaller_num = bin(min(num1, num2))[2:]
    length_diff = len(greater_num) - len(smaller_num)
    smaller_num = '0'*length_diff + smaller_num  # 使得两个数位数相等
    result = []
    C_in = 0
    # 从最低位开始，不停的使用普通的adder，同时将每个位置的计算结果保存在result列表里
    for i in range(1, len(greater_num)+1):
        i = -i
        A = int(smaller_num[i])
        B = int(greater_num[i])
        S, C_out = adder(A, B, C_in)
        result.append(str(S))
        C_in = C_out
    result.append(str(C_in))
    result.reverse()
    result = int(''.join(result), 2)
    return result


assert adder(0,0,0) == (0, 0)
assert adder(1,0,0) == (1, 0)
assert adder(0,1,0) == (1, 0)
assert adder(1,1,0) == (0, 1)
assert adder(1,0,1) == (0, 1)
assert adder(0,1,1) == (0, 1)
assert adder(1,1,1) == (1, 1)

assert arbitrary_length_adder(2, 6) == 8
assert arbitrary_length_adder(234, 10) == 244
