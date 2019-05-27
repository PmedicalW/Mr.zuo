"""
为两个已有功能（进入后台，删除订单），增加新的功能（验证权限）
"""
def get_root(func):

    def wrapper(*args, **kwargs):
        print("验证权限...")
        return func(*args, **kwargs)
    return wrapper

@get_root
def enter_background(loginId,pwd):
    print(loginId,pwd)
    print("进入后台系统...")

@get_root
def delete_order(order_id):
    print("删除%d号订单..."%order_id)

enter_background(000,123)
delete_order(1)






















