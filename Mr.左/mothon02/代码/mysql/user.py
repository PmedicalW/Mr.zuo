"""
１．创建一个数据表为user
２．编写程序完成如下功能：
    ＊注册，从终端输入用户名和密码，将用户名密码存入到数据库中，用户名不能重复
    ＊登录，从终端输入用户名和密码，如果该用户存在则得到登录成功，不存在则得到登录失败
３．将数据库操作功能封装成类
"""
from log_in import Login

user = Login()


# 　成功返回Ｔｒｕｅ失败返回Ｆａｌｓｅ
def do_login():
    name = input("User: ")
    passwd = input("Passwd: ")
    return user.login(name, passwd)


def do_register():
    name = input("User: ")
    passwd = input("Passwd: ")
    return user.register(name, passwd)


while True:
    print("=====================")
    print("**     login     ***")
    print("**    register   ***")
    print("=====================")

    cmd = input("Cmd:")
    if cmd == 'login':
        if do_login():
            print("登录成功")
        else:
            print("登录失败")
        break
    elif cmd == 'register':
        if do_register():
            print("注册成功")
        else:
            print("注册失败")
        break
    else:
        print("重新输入")

user.close()
