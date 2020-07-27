# 形参角度
# 万能参数

def eat(a,b,c,d):
    print('我请你吃：%s %s %s %s' %(a,b,c,d))

eat('西红柿','黄瓜','葡萄','黄桃')
# 急需一种形参，可以接受所有的实参
# 万能参数 *args 约定俗称 args
# * 函数定义时， *代表聚合 它将所有的位置参数聚合成一个元祖 赋值给args
def eat(*args):
    print(args)
    print('我请你吃：%s %s %s %s %s ' %args)

eat('西红柿','黄瓜','葡萄','黄桃','红提')

# 写一个函数 计算传入的所有的数字的和
def sumFunc(*args):
    count = 0;
    for i in args:
        count = count +i
    return count;

print(sumFunc(1,2,3,4,5))

# **kwargs
# 函数定义时，**将所有的关键字参数聚合到一个字典中  将这个字段赋值给kwargs

def func(**kwargs):
    print(kwargs)
func(name='sa',age=18) #{'name': 'sa', 'age': 18}

# 形参角度的参数的顺序
def func(*args,a,b,sex='boy'):
    print(a,b)

# func(1,2) #TypeError: func() missing 2 required keyword-only arguments: 'a' and 'b'

def func(a,b,*args,sex='boy'):
    print(a,b)
    print(args)
    print(sex)
func(1,2,3,4,5,6,sex='girl')

## **kwargs

def func(a,b,*args,sex='boy',**kwargs):
    print(a,b)
    print(args)
    print(sex)
    print(kwargs)
func(1,2,3,4,5,6,sex='girl',name='s',age=18)

## 形参角度第四个参数仅限关键字参数  c 不能不传
def func(a,b,*args,sex= '男',c,**kwargs):
    print(a,b)
    print(sex)
    print(args)
    print(c)
    print(kwargs)
func(1,2,3,4,5,6,7,sex='女',name='sa',age=18,c='666')

# 形参角度最终的顺序：位置参数,*args,默认参数，仅限关键字参数，**kwargs