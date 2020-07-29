# 用一行代码构建一个比较复杂有规律的列表
# 列表推导式
ll = [i for i in range(1,22)]
# 列表推导式分类
# 循环模式
# 将10以内所有的整数平方写入列表
ll = [i**2 for i in range(1,11)]
print(ll) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
# 100以内所有的偶数写入列表
ll = [i for i in range(2,101,2)]
print(ll)
# 从python1到python100写入列表
ll = [f'python{i}' for i in range(1,101)]
print(ll)

# 筛选模式
# 30以内能被3整除的数
l1 = [i for i in range(1,31) if i%3==0]
print(l1) #[3, 6, 9, 12, 15, 18, 21, 24, 27, 30]

# 过滤掉长度小于3的字符串，并将剩下的转换成大写
ll = ['andy','posd','post','master','ms']
l2 = [i.upper() for i in ll if len(i)>3]
print(l2) #['ANDY', 'POSD', 'POST', 'MASTER']

# 含有2个e的名字全大写留下来
# names = [['daeds','eeaws','oiewa','poese'],['aaeds','eedws','ovewa','poeae']]
# l1 = []
# for i in names:
#     for name in i :
#         if name.count('e') == 2:
#             l1.append(name.upper())
# print(l1)
# 多层循环的列表推导式
names = [['daeds', 'eeaws', 'oiewa', 'poese'], ['aaeds', 'eedws', 'ovewa', 'poeae']]
print([name.upper() for i in names for name in i if name.count('e')==2])


# 生成器表达式
# 与列表推导式的写法几乎一模一样
print([i for i in range(10)]) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print((i for i in range(10))) #<generator object <genexpr> at 0x000001FEA317E0F8>
obj = (i for i in range(10))
print(next(obj)) #0

# 总结
# 列表推导式
    # 1.有毒列表推导式只能构建比较复杂并且具有规律的列表
    # 2.超过三层才能构建的 不建议使用
    # 3.查找错误是不行的
    #优点：
        # 简单 一行构建
# 构建一个列表：【2,3,4,5,6,7,8,9,10，'j','q','k','A'】
l1 = [i for i in range(2,11)]+list('JQKA')
print(l1) #[2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
# 列表推导式与生成器表达式区别
# 写法上 [] ()
# iterable iterator