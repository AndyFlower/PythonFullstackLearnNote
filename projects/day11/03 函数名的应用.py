def  func():
    print(888)

#func()
# 1.函数名指向的是函数的内存地址
#函数名+（）就可以了执行次函数
a =1
#a() #TypeError: 'int' object is not callable
print(func) #<function func at 0x000002022EAE6EA0>
print(func,type(func)) #<function func at 0x0000026BEC156EA0> <class 'function'>

# 函数名就是变量
a=2
b=1
c=b
print(c)

f = func
f1=f
f2=f1
f()

def func():
    print('in func')

def func1():
    print('in func1')

func1=func
func1() #in func

# 函数名可以作为容器类数据类型的 元素
def func2():
    print('in func2')

def func1():
    print('in func1')

def func3():
    print('in func3')
ll = [func1,func2,func3]

for i in ll: # 批量执行函数
    i()

# 函数名可以作为函数的参数
def func(a):
    print(a)
    print('in func')
b=3
func(b)
print(func) #<function func at 0x000001959C2B01E0>

def func():
    print('in func')
def func1(x):
    x()

func1(func)

