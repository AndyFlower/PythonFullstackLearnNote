i1 = 2
i2 = 3
# print(2**3)

count = 1
count = count+1
count += 1
print(count)

# and or

# 在没有（）的情况下 优先级not > and > or
# 情况1 两边都是比较运算
print(2 > 1 and 3 < 4 or 4 > 5 and 2 < 1) #True
# 情况2  两边都是整数
# x or y x为真，值就是x  x为假 则为y
print(1 or 2) #1
print(3 or 2) # 3

# str->int   只能是纯数字组成的字符串才能转
print(int('2'))

# int-->str
i1 = 100
print(str(i1) , type(str(i1)))  # 100 <class 'str'>

# int -->bool 非0即为true 0为false
i = 1
print(bool(i)) # True
# bool -->int
print(int(True)) # 1