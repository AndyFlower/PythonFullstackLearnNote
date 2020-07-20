tu = (100,'sang',True,[1,2,3])
print(tu[0]) #100
print(tu[:3]) #(100, 'sang', True)


# 查看
for i in tu:
    print(i)


# 长度
print(len(tu)) #4

# 删除 不支持

# 应用
# 重要数据 用户名 密码个人信息不想让别人改动的 存在元祖中
# 元祖的拆包 分别赋值
a,b=(1,2) # 这里要一一对应
print(a,b) # 1 2

