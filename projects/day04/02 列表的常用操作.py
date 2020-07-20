# 列表的创建
# 方式1
li = [1,2,'sang']
#方式二
li = list('21wqewqewq')

#方式三 列表推导式

# 增删改查
l1 = ['孙悟空','沙僧','唐僧']

# 增 append:增加
l1.append('白龙马')
print(l1)
# print(l1.append('a')) 不能打印这个append操作

# 举例
l1 = ['s','l']
while 1 :
    name = input('请输入员工姓名，（Q或者q退出程序）')
    if name.upper() == 'Q':
        print(l1)
        break;
    l1.append(name)


# insert 插入
l1 = ['孙悟空','沙僧','唐僧']
l1.insert(1,'玉皇大帝')

# extend 迭代增加
l1.extend(['白骨精','牛魔王'])
print(l1)

# 删
# pop 安装索引位置删
l1.pop(-2)# 返回的是删除的元素 print(l1.pop(-2))
print(l1)
l1.pop()# 默认删除最后一个

# remove 指定元素删除 如果有重名元素，默认删除从左数第一个  如果元素不存在，会报错
l1.remove('沙僧')

# clear() 清空
l1.clear()
print(l1)

#del
'''
del按照索引删除
del l1[-1]
按照切片删除
del l1[::2]
'''

# 修改
l1 = ['孙悟空','沙僧','唐僧']
l1[0]='齐天大圣'
print(l1)
# 按照切片改
l1[2:]='sdadsad'
print(l1)
# 按照步长 元素必须一一对应

# 查
# 索引、切片（步长）
for i in l1:
    print(i)