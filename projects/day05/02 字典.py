# 不可变
s ='san'
s2 = s.upper();
print(s) #san

# 可变
li = [1,2,3]
li.append(4)
print(li) # [1, 2, 3, 4]

dict = {'sang':{'name':'sang','age':18},
 '语言':{'python','java','c++'}
 }

## 字典的创建方式
# 方式一
dic = dict((('one','1'),('two',2),('three',3)))
print(dic)
# 方式二
dic = dict(one = 1,two=2,three=3)
print(dic)

#方式3
dic = dict({'one':1,'two':2,'three':3})
print(dic)