# python提供了68个内置函数
# eval 又返回值
s1 = '1+3'
print(s1) #1+3
print(eval(s1)) #4

s = '{"name":"alex"}'
print(s,type(s)) #{"name":"alex"} <class 'str'>
print(eval(s)) #{'name': 'alex'}


# exec 与eval几乎一样 代码流
msg = """
for i in range(10):
    print(i)
"""
exec(msg)

#hash 获取一个对象的hash值
print('das')

#help
print(help(str.upper))

