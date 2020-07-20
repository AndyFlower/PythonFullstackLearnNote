r = range(10)
print(r) #range(0, 10)

for i in r:  # 0~9
    print(i)

# 索引
print(r[2]) # 2

# 两个参数 左闭右开
for i in range(0,100):
    print(i)

# 步长
for i in range(2,101,2):
    print(i)

# 逆向
for i in range(100,0,-1):
    print(i)


li = [1,2,3,'sang','太阳']
# 利用for循环 利用range将li所有元素索引打印出来

for i in range(len(li)):
    print(i)