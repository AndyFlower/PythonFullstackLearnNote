msg2 = '''
Name :sang
Age  :18
Job  :Teenager
'''

# 格式化输出
name = input('请输入姓名')
age = input('请输入年龄')
job = input('请输入工作')
msg = '''
Name :%s
Age  :%s
Job  :%s
'''
print(msg %(name,age,job))