# id 身份证号
i = 100
s = 'alex'
print(id(i)) #8791110722304
print(id(s)) #38402416

# == 比较的是两边的值是否相等
l1 = [1,2,3]
l2 = [1,2,3]
print(l1 == l2) #True
s1 = 'alex'
s2 = 'alex '
print(s1 == s2) #False

# is 判断的是内存地址是否相同
l1 = [1, 2, 3]
l2 = [1, 2, 3]
print(id(l1)) #40839552
print(id(l2)) #41022528
print(l1 is l2) #False

s1 = 'alex'
s2 = 'alex'
print(id(s1)) # 31193456
print(id(s2)) # 31193456
print(s1 is s2) # True

# id 相同，值一定相同
# 值相同，id不一定相同