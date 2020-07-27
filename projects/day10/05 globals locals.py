a=1
b=2
def funnc():
    name = 'sang'
    age =18
    print(globals())
    print(locals())
print(globals())# 返回的是字典 字典里面的键值对：全局作用域的所有内容
print(locals()) # 返回的是字典 字典里面的键值对是当前作用域的所有的内嵘