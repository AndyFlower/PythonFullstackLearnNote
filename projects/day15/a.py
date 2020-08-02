'''
自定义模块
模块中出现的变量，for循环 if结构 函数定义称为模块的成员
'''
# 可执行语句
a=1
print(a)

## 定义一个函数 包含测试语句
def main():
    print(a)
for i in range(3):
    print(i)
# 函数定义
def func():
    print('hello')

if __name__ =='__main__':
    main()