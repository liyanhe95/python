import unittest
import json
from ddt import ddt,data
from common import contants
from common.do_excel import DoExcel
from common.request import Request
from common.mysql import MysqlUntil
from common import context
max_mobile = None

@ddt
class TestRegister(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_data('register')

    @classmethod
    def setUpClass(cls):
        cls.request = Request()  # 它是一次会话，会把每次请求的cookie保存起来
        cls.mysql = MysqlUntil()

    @data(*cases)
    def test_register(self,item):
        print("开始执行第{}用例".format(item.id))
        sql = 'SELECT max(MobilePhone) FROM future.member WHERE MobilePhone LIKE"136%"'
        max = self.mysql.fetch_one(sql)
        max_mobile = int(max) + 1
        data_dict = json.loads(item.data)  # Excel字符串转成字典
        if data_dict['mobilephone'] == '${register_mobile}':  # 判断是否等于标记
            data_dict['mobilephone'] = max_mobile  # 将最大手机号码+1 赋值给mobilephone
        data_dict = json.dumps(data_dict)  # 把字典转换成字符串传入context进行转换
        data_new = context.replace_new(data_dict)
        resp = self.request.request(item.method,item.url,data_new) # 这里注意要传做过特换的字典！！！！
        print(resp.text)
        try:
            self.assertEqual(item.expected,resp.text,'register error')
            self.do_excel.write_result('register',item.id+1,resp.text,'PASS')
            print("第{}用例执行结果：PASS".format(item.id))
        except AssertionError as e:
            self.do_excel.write_result('register',item.id+1,resp.text,'FAIL')
            print("第{}用例执行结果：FAIL".format(item.id))
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()
        cls.request.session.close()  # 用完记得关闭session

