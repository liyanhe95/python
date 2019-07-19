#http协议两大部分
#requests：
#请求方法
#get 查获取资源
#post 改修改资源
#put 增加
#delete 删除
#option 获取可以支持的请求方式（后端的）
#header 返回的头部信息
#请求url  协议://服务器ip:// 端口号://接口路径
#请求参数：传参方式  表单传参和url传参
#header 请求头
#content-type
#user-agent 记录你的请求是从哪里发起的
#cookie  是存放在客户端的

#response
#状态码
#1 类是属于信息类  表示浏览器已经收到请求，正在处理信息
#2 类是成功类 表示用户请求被正确接收，理解和处理 eg:200 ok
#3 重定向类 表示请求没有成功，客户必须采取进一步的动作
#4 客户端错误类 表示客户端请求有错
#5 服务器错误  表示服务器不能完成对请求的处理

#响应信息
#cookie
#header

# 数据校验
#1 判断状态
#2 响应信息
#3 判断数据库

# import requests
# headers = {"cookie":"SESSION=4b17-a2e2-4003-345t","Host":"uuu.quick.com","Referer":"http://uuu.quick.com/login"}
# data = {"userid":"lilei","password":"123456","type":"login"}
# requests.post('http://10.221.138.22',data = data,headers = headers)
#

import requests

# url2 = "http://test.lemonban.com/futureloan/mvc/api/member/register"
# data2 = {"mobilephone":"18877314372","pwd":"123456@12","regname":"huahua"}
# res2 = requests.get(url=url2,params=data2)
# print(res2.text)
#第一步  构造请求
#用户登录
url = "http://test.lemonban.com/futureloan/mvc/api/member/login"
data = {"mobilephone":"18877314371","pwd":"123456"}
res = requests.get(url=url,params=data)
# # cookies = res.cookies
# print(res.text)
# print(res.cookies)
#用户取现
url2 = "http://test.lemonban.com/futureloan/mvc/api/member/withdraw"
data2 = {"mobilephone":18877314371,"amount":500000}
res2 = requests.get(url=url2,params=data2,cookies = res.cookies)
print(res2.text)
#用户充值
# url3 = "http://test.lemonban.com/futureloan/mvc/api/member/list"
# data3 = {"mobilephone":"13670287382","amount":30.569}
# res3 = requests.get(url=url3, params=data3,cookies=res.cookies)
# print(res3.text)
#新建项目
# data2 = {"memberId":2113,"title":111,"amount":100,"loanRate":18.0,"loanTerm":6,"loanDateType":0,"repaymemtWay":4,"biddingDays":4}
# url2 = "http://test.lemonban.com/futureloan/mvc/api/loan/add"
# res2 = requests.get(url=url2,params=data2,cookies=res.cookies)
# print(res2.text)

#审核
# data3 = {"id":2113,"status":4}
# url3 = "http://test.lemonban.com/futureloan/mvc/api/loan/audit"
# res3 = requests.get(url=url3,params=data3,cookies=res.cookies)
# print(res3.text)
# # 用户投标
# url3 = "http://test.lemonban.com/futureloan/mvc/api/member/bidLoan"
# data3 = {"memberId":2113,"password":123456,"loanId":2685,"amount":100}
# res3 = requests.get(url=url3, params=data3,cookies=res.cookies)
# print(res3.text)
