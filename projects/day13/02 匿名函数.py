# 匿名函数 ：一句话函数 比较简单
def func(a,b):
    return  a+b
#构建匿名函数 lamdba 参数：返回
func1 = lambda a,b :a+b
print(func1(1,2))

# 接收一个可切片的数据，返回索引0和2的位置的元素
func2 = lambda a:(a[0],a[2])
print(func2('abc'))

# 写匿名函数，接收2个int 返回较大的
func3 = lambda a,b:a if a>b else b;
print(func3(3,4))