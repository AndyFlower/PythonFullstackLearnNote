# str 补充的方法
s1 = 'adsSaad'
print(s1.capitalize()) #Adssaad  首字母大写，其余小写
print(s1.swapcase()) #ADSsAAD 翻转

msg = 'sang li ping'
print(msg.title()) #Sang Li Ping 每个单词首字母大写

s1 = 'barry'
print(s1.center(20)) # barry 居中
print(s1.center(20,'*')) # *******barry********

# find index  find找不到返回-1  index 找不到则报错
print(s1.find('a')) #1
print(s1.find('r')) #2
print(s1.find('g')) #-1 找不到返回-1

#tuple 元祖中如果只有一个元素 并且没有逗号，那么他不是元祖 与他的元素类型一致
tu1= (2)
print(tu1,type(tu1)) #2 <class 'int'>
tu1 = ('sa')
print(tu1,type(tu1)) #sa <class 'str'>
#count 计数
tu = (1,2,3,2,1,2,3)
print(tu.count(2))#3

tu = ('s','a','s')
print(tu.index('s')) #0

# list
l1 = ['sa','12','nv','li']
# count
# index
print(l1.index('12')) #1
# sort
l1 = [1,3,2,6]
l1.sort()
print(l1) #[1, 2, 3, 6]
l1.sort(reverse=True) # 从大到小
print(l1) #[6, 3, 2, 1]
l1 = [1,3,2,6]
l1.reverse() #反转
print(l1) #[6, 2, 3, 1]

# 列表相加
l1 = [1,2,3]
l2 = ['s','l','p']
print(l1+l2) #[1, 2, 3, 's', 'l', 'p']

# 列表与数字相乘
l3 = l1*2
print(l3) #[1, 2, 3, 1, 2, 3]

l1 =[11,22,33,44,55,66]
#索引奇数的删除
#方法1
#del l1[1::2]
for index in range(len(l1)-1,-1,-1):
    print(index)
    if index%2==0:
        l1.pop(index)
print(l1)

# 字典的补充
dic = {'name':'sa','age':18}
dic.update(hobby='yund',height=185)
print(dic) #{'name': 'sa', 'age': 18, 'hobby': 'yund', 'height': 185}

dic = dict.fromkeys('name',100)
print(dic) #{'n': 100, 'a': 100, 'm': 100, 'e': 100}

dic = dict.fromkeys([1,2,3],[])
print(dic) #{1: [], 2: [], 3: []}
dic[1].append(222) #{1: [222], 2: [222], 3: [222]}
print(dic)

dic = {'k1':'v1','k2':'v2','k3':'v4','age':18}
# 将含有k的键删除 RuntimeError: dictionary changed size during iteration
#for key in dic.keys():
#    if 'k' in key:
#        dic.pop(key)
#print(dic)

#循环字典时 如果改变这个字典的大小就会报错
ll=[]
for key in list(dic.keys()):
    if 'k' in key:
        dic.pop(key)
print(dic)


# 0 '' () [] {} set() None  转bool为false