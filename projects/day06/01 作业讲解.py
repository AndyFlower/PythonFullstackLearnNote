# 请将列表中的每个元素通过 "_" 链接起来。
#
users = ['李少奇','李启航','渣渣辉']
# 请将列表中的每个元素通过 "_" 链接起来。
print("_".join(users))
#
users = ['李少奇','李启航',666,'渣渣辉']
# users[-2] = '666'
# s = '_'.join(users)
# print(s)
# s = 'alex'
# print(str(s))
# 方法二
# s = ''
# for i in users:
#     s = s + '_' + str(i)
# print(s)
s = ''
for index in range(len(users)):
    if index == 0:
        s += str(users[index])
    else:
        s = s + '_' + str(users[index])
print(s)


# 请将元组 v1 = (11,22,33) 中的所有元素追加到列表 v2 = [44,55,66] 中。
v1 = (11,22,33)
v2 = [44,55,66]
for i in v1:
    v2.append(i)
print(v2)
v2.extend(v1)
print(v2)
#
# # 请将元组 v1 = (11,22,33,44,55,66,77,88,99) 中的所有偶数索引位置的元素 追加到列表 v2 = [44,55,66] 中。
v1 = (11,22,33,44,55,66,77,88,99)
v2 = [44,55,66]
# # print(v1[::2])
v2.extend(v1[::2])
print(v2)
# 将字典的键和值分别追加到 key_list 和 value_list 两个列表中，如：
#
key_list = []
value_list = []
info = {'k1':'v1','k2':'v2','k3':'v3'}
key_list.extend(info.keys())
value_list.extend(info.values())
print(key_list)
print(value_list)


# 字典dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
#
# a. 请循环输出所有的key
dic = {'k1': "v1", "k2": "v2", "k3": [11,22,33]}
for key in dic.keys():
    print(key)
# b. 请循环输出所有的value
for val in dic.values():
    print(val)
# c. 请循环输出所有的key和value
for key,val in dic.items():
    print(key,val)
# d. 请在字典中添加一个键值对，"k4": "v4"，输出添加后的字典
dic['k4']='v4'
print(dic)
# e. 请在修改字典中 "k1" 对应的值为 "alex"，输出修改后的字典
dic['k1']='alex'
print(dic)
# f. 请在k3对应的值中追加一个元素 44，输出修改后的字典
#dic['k3']=dic.get('k3').append(44)
ll = dic.get('k3')
ll.append(44)
dic['k3']=ll
print(dic)
# g. 请在k3对应的值的第 1 个位置插入个元素 18，输出修改后的字典
ll = dic.get('k3').insert(0,18)
print(dic)
av_catalog = {
    "欧美":{
        "www.太白.com": ["很多免费的,世界最大的","质量一般"],
        "www.alex.com": ["很多免费的,也很大","质量挺好"],
        "oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"],
        "hao222.com":["质量很高,真的很高","全部收费,屌丝请绕过"]
    },
    "日韩":{
        "tokyo-hot":["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]
    },
    "大陆":{
        "1024":["全部免费,真好,好人一生平安", "服务器在国外,慢"]
    }
}
# 给此 ["很多免费的,世界最大的","质量一般"]列表第二个位置插入一个 元素：'量很大'。
#
# 将此 ["质量很高,真的很高","全部收费,屌丝请绕过"]列表的 "全部收费,屌丝请绕过" 删除。
#
# 将此["质量怎样不清楚,个人已经不喜欢日韩范了","verygood"]列表的 "verygood"全部变成大写。
#
# 给 '大陆' 对应的字典添加一个键值对 '1048' :['一天就封了']
#
# 删除这个键值对："oldboy.com": ["多是自拍,高质量图片很多","资源不多,更新慢"]
#
# 给此["全部免费,真好,好人一生平安","服务器在国外,慢"]列表的第一个元素，加上一句话：'可以爬下来'
dic = av_catalog['大陆']
li = dic['1024']
new_s = li[0] + '可以爬下来'
li[0] = new_s
print(av_catalog)

# dic = av_catalog['大陆']
# li = av_catalog['大陆']['1024']
# new_s = av_catalog['大陆']['1024'][0] + '可以爬下来'
# av_catalog['大陆']['1024'][0] = av_catalog['大陆']['1024'][0] + '可以爬下来'
# l2 = [11,22]
# l2[0] = 66
# av_catalog['大陆']['1024'][0] +=  '可以爬下来'
# print(av_catalog)
# 请循环打印k2对应的值中的每个元素。
#
# info = {
#     'k1':'v1',
#     'k2':[('alex'),('wupeiqi'),('oldboy')],
# }
# 有字符串"k: 1|k1:2|k2:3 |k3 :4" 处理成字典 {'k':1,'k1':2....}
msg = "k: 1|k1:2|k2:3 |k3 :4"
'''
msg 按照 | 分隔： split  ['k: 1','k1:2','k2:3 ',k3 :4', ]
对每个元素进行操作 for循环 ...

'''
l1 = msg.strip().split('|')
dic = {}
# print(l1)
for i in l1:
    key,value = i.split(":")  # ['k', ' 1']
    dic[key.strip()] = int(value)
print(dic)
# 写代码
# """
# 有如下值 li= [11,22,33,44,55,66,77,88,99,90] ,将所有大于 66 的值保存至字典的第一个key对应的列表中，将小于 66 的值保存至第二个key对应的列表中。
# result = {'k1':[],'k2':[]}
# """
li= [11,22,33,44,55,66,77,88,99,90]
l1 = []
l2 = []
result = {'k1':[],'k2':[]}
for i in li:
    if i > 66:
        l1.append(i)
    else:
        l2.append(i)
result['k1']=l1
result['k2']=l2
print(result)
# 输出商品列表，用户输入序号，显示用户选中的商品
#
# """
# 商品列表：
#   goods = [
# 		{"name": "电脑", "price": 1999},
# 		{"name": "鼠标", "price": 10},
# 		{"name": "游艇", "price": 20},
# 		{"name": "美女", "price": 998}
# 	]
# 要求:
# 1：页面显示 序号 + 商品名称 + 商品价格，如：
#       1 电脑 1999
#       2 鼠标 10
# 	  ...
# 2：用户输入选择的商品序号，然后打印商品名称及商品价格
# 3：如果用户输入的商品序号有误，则提示输入有误，并重新输入。
# 4：用户输入Q或者q，退出程序。
# """
# 看代码写结果

goods = [
 	{"name": "电脑", "price": 1999},
 	{"name": "鼠标", "price": 10},
 	{"name": "游艇", "price": 20},
 	{"name": "美女", "price": 998}
]
# 枚举
l1  = ['a','b','v']
for i in enumerate(l1,start=1):
    print(i)
for index in range(len(goods)):
    print(index+1,goods[index]['name'],goods[index]['price'])

for num,dic in enumerate(goods,start=1):
    print(num,dic['name'],dic['price'])
while True:
    choice_num = input('请输入商品序号：').strip()
    if choice_num.isdecimal():
        choice_num = int(choice_num);
        if 0<choice_num<len(goods):
            print('您选择的商品名称是{},价格是{}'.format(goods[choice_num-1]['name'],goods[choice_num-1]['price']))
        else:
            print('超出范围，重新输入')
    elif choice_num.upper()=='Q':
        break;
    else:
        print('输入有误')
# v = {}
# for index in range(10):
#     v['users'] = index
# print(v)