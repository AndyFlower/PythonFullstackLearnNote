#f1 = open('d:\te.txt',encoding='utf-8',mode='r') #OSError: [Errno 22] Invalid argument: 'd:\te.txt'
f1 = open('d:/te.txt',encoding='utf-8',mode='r')
content = f1.read()
print(content)
f1.close()
'''
open 内置函数，open底层调用的是操作系统的接口。
f1,变量，f1,fh,file_handler,f_h,文件句柄。 对文件进行的任何操作，都得通过文件句柄. 的方式。
encoding:可以不写，不写参数，默认编码本：操作系统的默认的编码
windows: gbk。
linux： utf-8.
mac ： utf-8.
f1.close() 关闭文件句柄。
'''