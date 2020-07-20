li = [100,'sang',True,[1,2,3]]
# 索引
print(li[0],type(li[0])) # 100 <class 'int'>
print(li[1],type(li[1])) #sang <class 'str'>

#切片
print(li[:2]) #[100, 'sang']

# 练习题
li = [1,3,2,'a',4,'b',5,'c']
# 通过对li切片形成新的列表[1,3,2]
# 通过对li切片形成新的列表['a',4,'b]
l2 = li[3:6]
print(l2) #['a', 4, 'b']
l3 = li[1:-2:2]
print(l3)#[3, 'a', 'b']
