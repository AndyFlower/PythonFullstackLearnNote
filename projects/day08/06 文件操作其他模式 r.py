# 读并追加  # 顺序不能错误。 文件不存在会报错
f = open('文件的写', encoding='utf-8', mode='r+')
content = f.read() # 这里是读 将光标移动到最后
print(content)
f.write('人的一切痛苦，本质都是对自己无能的愤怒。')
f.close()

# 错误示例：
# f = open('文件的读写', encoding='utf-8', mode='r+')
# f.write('人的一切痛苦,,,本质都是对自己无能的愤怒,,,')
# content = f.read()
# print(content)
# f.close()