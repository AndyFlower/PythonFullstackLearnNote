'''
测试自定义模块的导入
'''
# 自定义模块被其他模块导入时，其中的可执行语句会立即执行
import time

# python当中提供一种可以判断自定义模块是属于开发阶段还是运行阶段


#__main__:脚本方式运行时，固定的字符串__main__

# if __name__ =='__main__':
#     pass

# 使用自定义模块的成员
#import a
#print(a.a)

# 查看sys.path内容
import sys
print(sys.path)
print(__file__)# 当前文件的绝对路径

import os
# 使用os获取当前目录的父目录
os.path.dirname(__file__)



sys.path.append()