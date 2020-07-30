# 封闭的东西 保证数据的
l1 = []
def mage_average(new_value):
    l1.append(new_value)
    total = sum(l1)
    return total/len(l1)
print(mage_average(1000))
print(mage_average(2000))


# 方案二 数据安全 l1不能放在全局变量

def make_ac():
    l1 = []
    def average(new_value):
        l1.append(new_value)
        total = sum(l1)
        return total/len(l1)
    return average
avg = make_ac() # 这里返回的是average的函数名称
print(avg(1000))
print(avg(2000))

# 闭包：
# 闭包只能存在嵌套的函数中
# 内层函数对外层函数非全局变量的引用，就会形成闭包
# 被引用的全局变量也叫自由变量，这个自由变量会与内层函数产生一个绑定关系 自由变量不会在内存中消失
# 闭包的作用：保证数据的安全，
# 如何判断一个嵌套函数是不是闭包

# 用代码判断闭包
print(avg.__code__.co_freevars) #('l1',) 这个就是绑定的自由变量