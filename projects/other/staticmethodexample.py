class C(object):
    @staticmethod
    def f():
        print('staticmethod')

C.f() ## 静态方法无需实例化
cobj = C()
cobj.f() ## 也可以实例化后调用