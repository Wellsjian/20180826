"""
练习1.
    增加新功能--->>验证权限
    运用装饰器
    功能要讲究弹性，可去可留
"""

def verify_permissons(func): #提供旧功能
    def wrapper(*args,**kwargs):  #打包
        print("验证权限")
        return func()
    return wrapper
@verify_permissons
def enter_bachgroud(*args,**kwargs):
    print("进入后台系统")
@verify_permissons
def delete_order(*args,**kwargs):
    print("删除订单")

enter_bachgroud()




