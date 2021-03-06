s1 = 'python'
# 对字符串进行索引，切片出来的数据都是字符串类型
# 从左到右顺序 下标 索引
s2 = s1[2]
print(s2,type(s2)) #t <class 'str'>

s4 = s1[-1]
print(s4) #n

# 安装切片取值  左闭右开
s5 = s1[0:5]
print(s5) #pytho

s6 = s1[2:]
print(s6) # thon

# 切片步长
s7 = s1[:5:2]
print(s7) #  pto   2是步长

# 倒序
s8 = s1[-1:-6:-1]
print(s8) # nohty  不加-1不会报错 但没有输出

# 按索引 s1[index]
# 按照切片 s1[start:end]
# 按照切片正序 s1[start:end:步长]
# 按照切片负 s1[start:end:-2]

s = 'sanglp'
# 字符串常用方法
# 不会对原字符串进行任何操作 都是产生一个新的字符串
# upper lower
print(s.upper()) #SANGLP
print(s.lower()) #sanglp

# 应用
username  = input('输入用户名')
password  = input('输入密码')
code = 'Sadw'
youcode = input('输入验证码,不区分大小写')
if code.upper() == youcode.upper():
    if username == 'sang' and password == '12':
        print('成功')
    else:
        print('用户名密码错误')
else:
    print('验证码错误')

# startswith endswith
s = 'zixin'
print(s.startswith('z')) #True
print(s.startswith('zi')) #True

print(s.startswith('x',2,4)) #True

#replace  默认替换全部，如果加第三个参数次数 则从左往右依次替换几个
msg = 'sanglp要加油'
msg1 = msg.replace('sanglp','slp')
print(msg1) # slp要加油

# strip 去除空白 :空格 \t \n
s4 = ' sn\t'
print(s4.strip()) #sn

# 可以去除指定的字符  从前往后 从后往前去除包含的字符
s5 = 'sang自信lp'
print(s5.strip('sanglp')) #自信

# split  默认按照空格分隔 返回一个列表
#  str --> list
s6 = '自信 大方  美丽'
l = s6.split()
print(l) # ['自信', '大方', '美丽']
# 指定分隔符
s6 = ':自信：大方：美丽'
print(s6.split(':')) #['', '自信：大方：美丽']
print(s6.split(':',2)) #['', '自信：大方：美丽']

# join
s1 = 'sang'
s2 = '+'.join(s1)
print(s2,type(s2)) #s+a+n+g <class 'str'>
# 前提 列表中的元素必须都是字符串
l1 = ['s','l','p']
s3 = ":".join(l1)
print(s3)# s:l:p

# count
ms = 'sdadsvdsda'
print(ms.count('s')) #3

# format 格式化输出
# 第一种用法：
msg = '我叫{} 几年{} 性别{}'.format('sang',18,'girl')
print(msg)
#第二种方法
msg = '我叫{０} 几年{１} 性别{２}我叫｛０｝'.format('sang',18,'girl')
print(msg)
# 第三种
msg = '我叫{name} 几年{age} 性别{sex}'.format(name='sang',age=18,sex = 'girl')
print(msg)

# is 系列
name = 'sang1'
print(name.isalpha()) # 字母
print(name.isalnum())# 字母或数字
print(name.isdecimal())# 十进制
print(name.isdigit())
