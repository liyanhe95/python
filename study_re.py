import json
import re #使用正则
admin_user = "13670287382"
admin_pwd = "123456"
data = {"admin_user":"13670287382","admin_pwd":"123456"}
s = '{"mobilephone":"${admin_user}","pwd":"${admin_pwd}"}'
p = "\$\{admin_user}" #根据原本字符查找因为$是一个符号，如果要让正则表达式$作为一个字符处理的话，一定要记得转义一下
p1 = "\$\{(.*?)}" #根据元字符和限定符，()代表组,英文输入法下写正则表达式
m = re.search(p1,s)  #search任意位置开始找，找到一个就返回match对象
#如果只想要admin_user
print("匹配对象",m)
g = m.group() #返回的是整个匹配的字符串
print(g)
g1 = m.group(1)  #取一个组的匹配字符串
print(g1)
# value = data[g1]
# # s = s.replace("${admin_user}",value)
# s = re.sub(p1,value,s,count=1) #查找全部且替换
# print("使用正则表达式查找并且替换：",s)
list1 = re.findall(p1,s) #查找全部，返回一个列表
print(list1)

# 将字符串转成字典，然后根据key去取值，取到值判断是否是需要替换
# dict1 = json.loads(s)
# if dict1["mobilephone"] == "${admin_user}":
#     dict1["mobilephone"] = admin_user
#
# if dict1["pwd"] == "${admin_pwd}":
#     dict1["pwd"] = admin_pwd
#
# print(dict1)
# 字符串的查找，替换
# print(s.find('${admin_user}'))
# if s.find('${admin_user}') > -1:
#     s = s.replace('${admin_user}', admin_user)  # 一定要重新去赋值，因为字符串是不可以替换的
# if s.find('${admin_pwd}') > -1:
#     s = s.replace('${admin_pwd}', admin_pwd)
# print(s)  # 字符串是不可变的
#根据key，动态的去取值
#正则表达式使用单个字符串来描述，匹配一系列符合某个句法规则的字符串
#正则表达式一般包含原本字符和元字符两种
#（）表示一个组，通俗的理解就是可以用它来标记一个表达式组的开始和结束
# .  可以匹配任意单个字符，汉字，字母，符号，数字（注意就是一个）
# \d 匹配任意单个数字
#限定符
# +  至少匹配一次
# ？ 最多匹配一次
# *  匹配0次或多次
# data = {"admin_user":"13670287382","admin_pwd":"123456"}