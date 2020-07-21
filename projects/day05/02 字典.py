# 不可变
s ='san'
s2 = s.upper();
print(s) #san

# 可变
li = [1,2,3]
li.append(4)
print(li) # [1, 2, 3, 4]

dict1 = {'sang':{'name':'sang','age':18},
 '语言':{'python','java','c++'}
 }

## 字典的创建方式
# 方式一
dic = dict((('one',1),('two',2),('three',3)))
print(dic)
# 方式二
dic = dict(one = 1,two=2,three=3)
print(dic)

#方式3
dic = dict({'one':1,'two':2,'three':3})
print(dic)

dic = {1:'san',1:'taibai',2:'w'} # 键唯一
print(dic)

dic = {'name':'sang','age':18,'hobby_list':['1','2','3']}
# 增加  有则覆盖
dic['sex'] = '女';
dic['age']=20;# 会修改掉原来的值
# dic.setdefault() 有则不变 无则增加
dic.setdefault('hobby','运动')
print(dic)

# 删
# pop 按照键去删除
ret = dic.pop('age')
print(ret)
print(dic)
# 设置第二个参数  无论有没有此键 都不会报错
ret =dic.pop('hobby','没有此键')
print(ret)
print(dic)

# 改
dic['name']='anan'
print(dic)

#查
print(dic['hobby_list']) # 没有则报错

# get
ll = dic.get('hobby_list')
print(ll)
ll = dic.get('hobby_list','没有此键')

#keys()  values ()  items()

print(dic.keys())
print(list(dic.keys()))
for key in dic.keys():
    print(key)
print(dic.values())
print(list(dic.values()))

for i in dic.items():
    print(i)

for key,value in dic.items():
    print(key,value)

# clear  清空
dic.clear()
print(dic)

# del
del dic['age'] # 键必须存在

# 面试题 使用ab互换
a = 18
b = 12
a,b = b ,a
print(a,b)

# 练习题
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
# 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic['k4']='v4'
print(dic)
# 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic['k1']='alex'
print(dic)
# 请在k3对应的值中追加一个元素 44，输出修改后的字典
dic['k3']=dic.get('k3').append(44)
print(dic)
# 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典