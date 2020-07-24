s1 = '2123212312'
# python没有len 自己写
count = 0;
for i in s1:
    count =count+1;
#print(count)

ll = [1,2,3,4,5,6];
count = 0;
for i in ll:
    count+=1;
#print(count)

#函数已功能为导向 一个函数只做一个功能
def mylen(s):
    count = 0;
    for i in s :
        count+=1
    return count

print(mylen(s1))
print(mylen(ll))

def meet():
    print('打开软件')
    print('左滑一下')
    print('右滑一下')
    print('找朋友')
    print('say hello')
    print('交朋友')
    return '大咖'
'''
结构：def 关键字 定义函数
meet:函数名：与变量设置相同，具有可描述性
函数体：缩进 函数中尽量不要出现print
'''

# 函数什么时候执行
meet()
print(meet())