f = open('文件的读.txt',encoding='utf-8')
content = f.read()
print(content)
f.close()

# read(n)
f = open('文件的读.txt',encoding='utf-8')
content = f.read(1)
print(content)
f.close()

f = open('文件的读.txt',encoding='utf-8')
#content = f.readlines()
content = f.readline()
print(content)
f.close()

#readlines 读取
f = open('文件的读.txt',encoding='utf-8')
ll =f.readlines()
for line in ll:
    print(line)
f.close()

f = open('文件的读.txt',encoding='utf-8')
for line in f:
    print(line)
f.close()

f = open('20200522165941.jpg',mode='rb')
content = f.read()
print(content)
f.close()
