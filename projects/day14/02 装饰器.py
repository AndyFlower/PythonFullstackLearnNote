# 装饰器 装饰
# 装饰器 ： 完全遵循开放封闭原则
# 装饰器：在不改变2函数的代码以及方式的前提下，为其增加新的功能
# 装饰器就是一个函数
# 写代码测试函数执行效率
import time
def index():
    time.sleep(3)
    print('欢迎')

start = time.time()
index()
end  = time.time()
print(end-start)


# versio2 解决代码重复
def timer(f):
    start = time.time();
    f()
    end = time.time()
    print(end-start)

timer(index)

# 有问题 改变了原函数的调用方式 原函数的调用方式修改成闭包的方式
def timernew(f):
    def inner():
        start = time.time();
        f()
        end = time.time()
        print(end-start)
    return inner()
#timernew(index)
index = timernew(index)
index()

def func():
    print('in func')

def func1():
    print('in func1')
func()
func=66 # func原本指向一个函数地址 现在指向了字符串
func(0) # 不能执行