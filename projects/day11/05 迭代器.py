s1 = 'fjdskl'
l1 = [1,2,3]
print(dir(s1))
print(dir((l1)))
print('__iter__' in dir(s1))
print('__iter__' in dir(range(10)))

s = '212'
print('__next__' in dir(s)) #False

# 可迭代对象可以转化成迭代器
s1='223'
obj = iter(s1) # s1.__iter__()
print(obj) # <str_iterator object at 0x0000029623BC10F0>
print(obj.__next__()) #2
print(next(obj)) #2
print(next(obj)) #2
print(next(obj)) #3
#print(next(obj)) ## StopIteration
ll=[11,22,33,44]
obj1 = iter(ll)
print(next(obj1))

# while 模拟for循环
l1 = [11,22,33,44,55,66,77,88,99,1111,1133,15652]
# 将可迭代对象转化成迭代器。
obj2 = iter(l1)
while 1:
    try:
        print(next(obj2))
    except StopIteration:
        break