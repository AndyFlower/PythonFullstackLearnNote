# crtl+？注销所有选中的行
# a = 1
# print(a)

# int主要用于计算  + - * /
# 不同的进制之间的转换  10进制  2进制

'''
二进制转换为十进制
0001 1010
'''
b = 2+2**3+2**4;
print(b)

'''
十进制转二进制 
辗转相除法
'''

# bit_length :有效的二进制长度
i = 4
print(i.bit_length()) # 3
i = 42
print(i.bit_length()) # 6

# bool str int
# bool <-> int

'''
True 1 False 0
非零为True 0是False
'''

'''
str <-> int
s1 = 10 
int(s1)
'''

'''
str bool
非空即为True
'''
s1 = ' '
print(bool(s1)) #True
s1 = ''
print(bool(s1)) #False

s = input("输入内容")
if s :
    print('有内容')
else:
    print('空')