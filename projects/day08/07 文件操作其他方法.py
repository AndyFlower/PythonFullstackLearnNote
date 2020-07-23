# tell 获取光标的位置 单位字节。
f = open('文件的写', encoding='utf-8')
print(f.tell()) #0
content = f.read()
print(content) #天天开心....人的一切痛苦，本质都是对自己无能的愤怒。
print(f.tell())#76
f.close()

# seek 调整光标的位置 seek(n)光标移动到n位置,注意: 移动单位是byte,所有如果是utf-8的中文部分要是3的倍数

# 通常我们使用seek都是移动到开头或者结尾

# 移动到开头:seek(0)

# 移动到结尾:seek(0,2) seek的第二个参数表示的是从哪个位置进行偏移,默认是0,表示开头,1表示当前位置,2表示结尾
f = open('文件的写', encoding='utf-8')
f.seek(2)
content = f.read()
print(content)
f.close()

# flush 强制刷新
# f = open('文件的其他功能', encoding='utf-8',mode='w')
# f.write('fdshdsjgsdlkjfdf')
# f.flush()
# f.close()