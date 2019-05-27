"""
为两个已有功能（存款，取款），添加新功能（验证账户）
"""
def verify_account(func):
    def wrapper(*args, **kwargs):
        print("验证账户...")
        return func(*args, **kwargs)
    return wrapper


@verify_account
def deposit(money):
    print("存款：",money)

@verify_account
def withdraw():
    print("取钱")
    return 10000

deposit(5000)
print(withdraw())





















