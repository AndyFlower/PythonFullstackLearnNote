# 名称空间
a = 1
b = 2
def func():
    f = 5
    print(f)
c=3
func()

# 内置名称空间：python源码提供的方法 参数等
# python分为三个空间
# 内置名称空间 builtins.py
#全局名称空间
# 局部名称空间 函数 函数执行时才开辟

# 作用域
# 两个作用域
 #全局作用域：内置名称空间  全局名称空间
 #局部作用域：局部名称空间

name = 'sang'
# 局部作用域不能改变全局作用域的变量，当python解释器读取到局部作用域时，发现了你对一个变量进行修改的操作，解释器会认为你在局部已经定义过这个局部变量了，他就从局部找这个变量，就会报错。
#def func():
    #name +='s';
    #print(name) # UnboundLocalError: local variable 'name' referenced before assignment


#func()
#
def  fund():
    count =1;
    def inner():
        print(count)# 引用可以 不能改变 如果修改会报错
    inner()
fund()

# LEGB原则  LOCAL  ECLOSE  GLOBAL BUILTIN
