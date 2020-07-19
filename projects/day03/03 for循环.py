s1 = 'sang'
print('s' in s1) #True
print('sg' in s1) #False
print('sg' not  in s1) #True

s1 = 'sanglp要自信'
i=0
while i<9:
    print(s1[i])
    i+=1

i=0
s = len(s1) # 获取可迭代对象的长度
while i<s:
    print(s1[i])
    i+=1


'''
有限循环
for 变量 in iterable:
    pass
'''

for s2 in s1:
    print(s2)

#　break  continue
for s2 in s1:
    if s2 =='l':
        break
    print(s2)
# for  else 和while  else一样