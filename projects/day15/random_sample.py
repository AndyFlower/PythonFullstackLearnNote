'''
random模块的示例

'''
import random
# 0到1的浮点数
print(random.random())
# 2到4中的整数
print(random.randint(2,4))
# 3到4中的浮点数
print(random.uniform(3,4))
lst = list(range(6))
# 数据打散
random.shuffle(lst)
print(lst)
t = (1,2,3)
lst = random.sample(t,len(t))
print(lst)