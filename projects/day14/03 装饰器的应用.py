# 装饰器的应用 登陆认证

login_status = False;

status_dict = {
    'username':None,
    'status':False
}
def auth(f):
    def inner(*args,**kwargs):
        if status_dict['status']:
            ret =f(*args,**kwargs)
            return ret
        else:
            username = input('请输入用户名').strip()
            password = input('请输入密码').strip()
            if username == 's' and password == '123':
                print('登录成功')
                login_status = True
                status_dict['username'] = username
                ret = f(*args,**kwargs)
                return ret
            else:
                print('登录失败')
    return inner;
@auth
def login():
    print('登陆')
@auth
def register():
    print('认证')
@auth
def article():
    print('欢迎访问文字')
@auth
def comment():
    print('欢迎访问文章')
@auth
def diary():
    print('欢迎访问日记')

login()
article()

