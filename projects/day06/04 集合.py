# 集合的创建
set1 = set({1,3,'sa'})
print(set1) # {1, 'sa', 3}
set2 = {1,2,3,'s','a'}
print(set2) #{1, 2, 3, 's', 'a'}

# 空集合
print({},type({})) # {} <class 'dict'>

set3 = set() #空集合
print(set3)

# 要求元素不可变 所以报错
#set4 = {[1,2,3],3,{'name':'sa'}}
#print(set4) #TypeError: unhashable type: 'list'

# 增
set5 = {'sang','李','赵'}
set5.add('王')
print(set5)

# update 迭代增加
set5.update('dasd');
print(set5)

# 删
set5.remove('s')
print(set5)

# 随机删除
set5.pop()
print(set5)

# 变相改
set5.remove('d')
set5.add('as')
print(set5)

# 交集

set6 = {1,2,3,4,5}
set7 = {4,5,6,7,8}
print(set6 & set7)
print(set6.intersection(set7))

#并集
print(set6 |set7)
print(set6.union(set7))
# 差集
print(set6-set7)
print(set6.difference(set7))

# 反交集
print(set6^set7) # {1, 2, 3, 6, 7, 8}

# 子集
set8 = {1,2,3}
set9 = {1,2,3,4,5,6}
print(set8<set9)

# 超集
print(set2>set1)

# 列表的去重
l1 = [1,2,3,1,2,3,5,6,6,7]
set1 = set(l1)
l1 = list(set1)
print(l1) #[1, 2, 3, 5, 6, 7]
