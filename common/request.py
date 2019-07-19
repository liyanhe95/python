import requests
import json
from common import logger
from common.config import ReadConfig

logger = logger.get_logger("request")

class Request:
    # 定义一个requests类
    def __init__(self):
        #实例化一个session对象，节省了后面两次接口调用的实例化的时间
        #浏览器作为客户端，第一次发送请求到服务端，登录成功会返回给浏览器一个cookie，浏览器会保存下来，下次再进去其它请求时，会自动带上去发给服务器端、
        #同一个session之间的cookie可以共享
        #session和cookie都是来自于服务端的，服务端要的时候必须要转，服务端不要的时候传进来也不会影响逻辑
        self.session = requests.sessions.session()  # 实例化一个session,建立一个session会话

    def request(self, method, url, data=None):
        method = method.upper()  # 将字符转换成大写  增强程序的健壮性
        config = ReadConfig()
        pre_url = config.get("api","pre_url")
        url = pre_url + url

        if data is not None and type(data) == str:
            #python中json和eval函数的区别：
            #1 json是跨语言的，而eval是python的函数，是基于python的格式进行转换的，用eval函数，
            # 只能是转换python格式的数据类型，eval的作用范围比较小，而eval函数的作用范围比较大，
            # json的跨语言的数据格式
            # data = eval(data) #如果是字符串就转回字典
            data = json.loads(data)  #如果是字符串就转回字典
        logger.info('method: {0}  url: {1}'.format(method, url))
        logger.info('data: {0}'.format(data))

        if method == 'GET':
            resp = self.session.request(method, url=url, params=data)# 调用get方法，使用params传参（url传参）
            logger.info('response: {0}'.format(resp.text))
            return resp

        elif method == 'POST':
            resp = self.session.request(method, url=url, data=data)# 调用post方法，使用data传参（表单传参）
            logger.info('response: {0}'.format(resp.text))
            return resp

        else:
            logger.info('un-support method!')

    def close(self):
        self.session.close()#关闭session

if __name__ == '__main__':
    request = Request()
    data = {"mobilephone": "13670287832", "pwd": "123456"}
    request.request('get',"http://test.lemonban.com/futureloan/mvc/api/member/login",data=data)