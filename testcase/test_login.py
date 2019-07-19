import unittest
from libext.ddtnew import ddt,data
from common import contants
from common.request import Request
from common.do_excel import DoExcel
from common import logger
#1.数据库中查询最大的手机号码+1
#2.case.data 里面的手机号码给替换掉
#3.然后去请求
#4.注册名可以使用随机字符，名字在数据库中一般不做唯一键
#DDT 数据驱动测试
#@ddt  测试类装饰器
#@data @unpack @file_data 测试方法装饰器
#1.读取单个数据
#2.读取多个数据
#3.读取文件数据  （json/yaml）
#parameterized 模块
#一个接口一个类，一个类一个方法
#一个类，多个方法，多个接口
#一个类，一个方法，全部接口
logger = logger.get_logger("login")#获取logger实例
@ddt
class LoginTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)  # 传入test.xlsx
    cases = do_excel.get_data('login')#定位表单
    request = Request() #实例化request

    def setUp(self):
        pass

    @data(*cases)
    def test_login(self,item):  #用一个变量来解释data传递的数据

        # 使用封装好的request 来完成请求
        logger.info("开始执行第{}用例".format(item.id))
        resp = self.request.request(item.method, item.url, item.data)
        # 将返回结果和期望结果进行匹配
        try:
            self.assertEqual(item.expected, resp.text, "login error")
            self.do_excel.write_result('login', item.id + 1, resp.text, 'PASS')
            logger.info("第{}用例执行结果：PASS".format(item.id))
        except AssertionError as e:
            self.do_excel.write_result('login', item.id + 1, resp.text, 'FAIL')
            logger.error("第{}用例执行结果：FAIL".format(item.id))
            raise e

    def tearDown(self):
        pass

