#str  是目标字符串
#dict 是替换的内容
# 转进来一个str 和 dict，找到目标字符串里面的标识符KEY，
# 去d里面拿到替换的值，替换到s里面去，然后再返回
import re
from common.config import ReadConfig
config = ReadConfig()

class Context:
    #这是一个上下文类，用于数据的准备和记录
    admin_user = config.get("data","admin_user")
    admin_pwd = config.get("data","admin_pwd")
    #loan_member_id 借款人的memberid
    loan_member_id = config.get("data","loan_member_id")
    # normal_user投资人
    normal_user = config.get("data","normal_user")
    normal_pwd = config.get("data","normal_pwd")
    # 投资人的normal_member_id
    normal_member_id = config.get("data","normal_member_id")\

    withdraw_phone = config.get("data","withdraw_phone")
    withdraw_pwd = config.get("data","withdraw_pwd")

    recharge_phone = config.get("data","recharge_phone")
    recharge_pwd = config.get("data","recharge_pwd")


def replace_new(s):
    p = "\$\{(.*?)}" #根据元字符和限定符，()代表组,英文输入法下写正则表达式
    while re.search(p,s):
        m = re.search(p,s)#search任意位置开始找，找到一个就返回match对象
        key = m.group(1) #取一个组的匹配字符串
        if hasattr(Context,key):#判断类是否有这个属性
            value = getattr(Context,key)  #根据属性名获取类的属性，动态的去获取(利用反射动态的获取属性)
            s = re.sub(p,value,s,count=1) #一定要重新赋值,sub是查找并且替换
        else:
            try:
                return None
            except AttributeError as e:
                print("no Attribute")
                raise e
             #或者抛出一个一次，告知没有这个属性
    return s


# def replace(s,dict):
#     p = "\$\{(.*?)}" #根据元字符和限定符，()代表组,英文输入法下写正则表达式
#     while re.search(p,s):
#         m = re.search(p,s)#search任意位置开始找，找到一个就返回match对象
#         key = m.group(1) #取一个组的匹配字符串
#         value = dict[key]
#         s = re.sub(p,value,s,count=1) #一定要重新赋值
#     return s
# s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
# data = {"admin_user":"13670287382","admin_pwd":"123456"}
# s = replace(s,data)
# print(s)
# s = replace_new(s)
# print(s)
#如何解决多个module，不同测试类之间的测试数据
#同一个类或者是module里面，不同方法之间的数据传递 A a B a global
#1global   设计loan_id 的全局变量，从数据库中查出来，然后赋值到全局变量中
#2 在另外一个sheet的 加标成功之后用到另外一个sheet  这种方式不可行