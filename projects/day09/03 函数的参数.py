# 实参角度
# 位置参数 从左到右 一一对应
def meet(gender):
    print('打开软件')
    print('筛选 %s' %(gender))
    print('左滑一下')
    print('右滑一下')
    print('找朋友')
    print('say hello')
    print('交朋友')
    return '大咖'

meet('8')
'''
函数的参数

'''


def meet(sex, age, skill, hight, weight, ):
    print('打开tantan')
    print('进行筛选：性别：%s,年龄：%s,技术：%s,身高：%s,体重%s' % (sex, age, skill, hight, weight))
    print('左滑一下')
    print('右滑一下')
    print('找朋友')
    print('悄悄话....')
    print('约....走起...')


meet(age=25, weight=100, hight=174, skill='python技术好的', sex='女')

#函数：传入两个字符串参数，将两个参数拼接完成后形成的结果返回。一一对应
def meet(sex, age, skill, hight, weight, ):
    print('打开tantan')
    print('进行筛选：性别：%s,年龄：%s,技术：%s,身高：%s,体重%s' % (sex, age, skill, hight, weight))
    print('左滑一下')
    print('右滑一下')
    print('找朋友')
    print('悄悄话....')
    print('约....走起...')


meet(age=25, weight=100, hight=174, skill='python技术好的', sex='女')

#函数：传入两个字符串参数，将两个参数拼接完成后形成的结果返回。
def func(a, b):
    return a + b


print(func(b='太白', a='无敌'))

def comp(a,b):
    if a>b:
        return a
    else:
        return b;
print(comp(10,20))

def compa(a,b):
    c = a if a>b else b; # 三元运算符
    return c;
print(compa(20,30))
# 混合参数
# 位置参数一定要在关键字参数的前面。
def meet(sex,age,skill,hight,weight,):
    print('打开tantan')
    print('进行筛选：性别：%s,年龄：%s,技术：%s,身高：%s,体重%s' %(sex,age,skill,hight,weight))
    print('左滑一下')
    print('右滑一下')
    print('找美女')
    print('悄悄话....')
    print('约....走起...')
    return '筛选结果：性别：%s,体重%s' %(sex,weight)

print(meet('女',25,weight=100,hight=174,skill='python技术好的'))
# 关键字参数
def meet2(sex, age, skill, height, weight ):
    print('打开tantan')
    print('进行筛选：性别：%s,年龄：%s,技术：%s,身高：%s,体重%s' % (sex, age, skill, height, weight))
    print('左滑一下')
    print('右滑一下')
    print('找朋友')
    print('悄悄话....')
    print('约....走起...')

meet2(sex='1',age=18,weight=100,height=180,skill='21')


'''
实参角度：
    1. 位置参数 按照顺序，一一对应
    2. 关键字参数， 一一对应
    3. 混合参数：位置参数一定要在关键字参数的前面。
'''

# 形参角度：
# 1，位置参数 与实参角度的位置参数是一种。

# def meet(sex,age,skill):
#     print('打开tantan')
#     print('进行筛选：性别：%s,年龄：%s,%s' %(sex,age,skill))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话....')
#     print('约....走起...')
#
# meet('女',25,'python技术好的',)
#
# 写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# def func(l):
#     if len(l) > 2:
#         return l[:2]
#     else:
#         return l
# # print(func([1,2,3,4,5]))
# print(func([1,]))
#
# def func(l):
#     c = l[:2] if len(l) > 2 else l
#     return c
# print(func([1,2,3,4,5]))
# print(func([1,]))
#
# def func(l):
#     return l[:2]
# # l1 = [1,]
# # print(l1[:2])

# 默认值参数
# 默认参数设置的意义：普遍经常使用的。
#
# def meet(age,skill='python技术好的',sex='女',):
#     print('打开tantan')
#     print('进行筛选：性别：%s,年龄：%s,技能：%s' %(sex,age,skill))
#     print('左滑一下')
#     print('右滑一下')
#     print('找美女')
#     print('悄悄话....')
#     print('约....走起...')
#
# # meet(25,'python技术好的',)
# meet(25,'运维技术好的','男')
#
# open()

# 形参角度：
# 1. 位置参数
# 2. 默认参数  （经常使用的参数）