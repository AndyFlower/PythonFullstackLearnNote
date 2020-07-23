content = input('>>>')

print(content,type(content)) # 中国 <class 'str'>
# str-->bytes
b1 = content.encode('utf-8')
print(b1) # b'\xe4\xb8\xad\xe5\x9b\xbd'
# bytes --->str
b2 = b1.decode('utf-8')
print(b2)