import copy;
class Bus:
    def __init__(self,passagers=None):
        if passagers is None:
            self.passagers=[]
        else:
            self.passagers = list(passagers)
    def pick(self,name):
        self.passagers.append(name)
    def drop(self,name):
        self.passagers.remove(name)

bus1 = Bus(['Alice','Bill','Claire','David'])
bus2= copy.copy(bus1) #浅拷贝
bus3 = copy.deepcopy(bus1) #深拷贝

print(id(bus1),id(bus2),id(bus3)) #2871541526368 2871541526480 2871541584672

bus1.drop('Bill')
print(bus2.passagers) #['Alice', 'Claire', 'David']

print(id(bus1.passagers),id(bus2.passagers),id(bus3.passagers)) #2871541471368 2871541471368 2871541469768

print(bus3.passagers) #['Alice', 'Bill', 'Claire', 'David']


class HauntedBus:
    """
    如果使用可变列表做默认参数，那么没有指定乘客的实例会共享同一个乘客列表
    """
    def __init__(self,passengers=[]):
        self.passengers = passengers
    def pick(self,name):
        self.passengers.append(name)
    def drop(self,name):
        self.passengers.remove(name)

bu1 = HauntedBus(['Alice','Bill']);
print(bu1.passengers) #['Alice', 'Bill']
bu1.pick('Charlie')
bu1.drop('Alice') #['Bill', 'Charlie']

print(bu1.passengers)

bu2 = HauntedBus()
bu2.pick('Carrie')
print(bu2.passengers) #['Carrie']

bu3 = HauntedBus()

print(bu3.passengers)#['Carrie']
bu3.pick('Dave')
print(bu2.passengers)#['Carrie', 'Dave']
print(bu2.passengers is bu3.passengers)

class  TwilightBus:
    def __init__(self,passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers=passengers ### 注意这里

    def pick(self,name):
        self.passengers.append(name)
    def drop(self,name):
        self.passengers.remove(name)