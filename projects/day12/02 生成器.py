# #函数
# def func():
#     print(111)
#     print(222)
#     return 3
#
# func()

#生成器函数
def func():
    print(111)
    print(222)
    yield 3
    yield 4
ret = func();
print(ret) #<generator object func at 0x000002C95D85E888>
print(next(ret)) #3 一个next对应一个yield
print(next(ret)) #4 如果next已经没有了则抛出异常 StopIteration

# return yield
#return :函数中只存在一个return结束函数，并且给函数的执行返回值
# yield：只要函数中有yield那么他就是生成器而不是函数了
# 生成器函数中可以存在多个yield yield不会结束生成器函数  一个yield对应一个next

# def func():
#     print(111)
#     return 222
#     yield 333
#
# ret = func()
# print(ret) #<generator object func at 0x0000021F8909E888>
# print(next(ret)) #StopIteration: 222

# ll = [12,3,4,5,6,7]
# print(iter(ll)) #<list_iterator object at 0x00000267299550F0>

# # 吃包子
# def func():
#     ll = []
#     for i in range(1,5001):
#         ll.append(f'{i}号包子')
#     return ll
# ret = func();
# print(ret) #['1号包子', '2号包子', '3号包子',

# def gen_func():
#     for i in range(1,5001):
#         yield f'{i}号包子'
# ret = gen_func()
# print(next(ret))#1号包子
# for i in range(10):
#     print(next(ret))# 2-11是有顺序的

# yield from
# def func():
#     l1 = [1,2,3,4,5]
#     #yield l1 [1, 2, 3, 4, 5]
#     yield from l1
#     # 将l1这个列表变成了一个迭代器返回
# ret = func()
# print(next(ret)) #1

def func():
    l1=[1,3,4,5]
    l2=[2,6]
    yield from l1
    yield from l2
    '''
    1
3
4
5
2
6
    '''
g = func()
for i in range(6):
    print(next(g))