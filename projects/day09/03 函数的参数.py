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