# 没有文件创建文件，追加内容
f = open('文件的追加',encoding='utf-8',mode='a')
f.write('天天向上....')
f.close()

# 有文件，在原文件的最后面追加内容。
f = open('文件的追加',encoding='utf-8',mode='a')
f.write('天天开心')
f.close()