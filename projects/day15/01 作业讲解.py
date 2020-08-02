def wrapper(f):
    def inner(*args,**kwargs):
        '''执行前的操作'''
        print(2)
        ret = f(*args,**kwargs)
        '''执行后的操作'''
        print(4)
        return ret
    return inner

@wrapper
def func():
    print('in func')

func()