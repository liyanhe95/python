import unittest
import json
from ddt import ddt,data
from common import contants
from common.do_excel import DoExcel
from common.request import Request
from common.mysql import MysqlUntil
max_mobile = None
@ddt
class TestRegister(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_data('register')

    def setUp(self): #setUP 方法每个TestCase方法执行之前执行一次
        sql = 'SELECT max(MobilePhone) FROM future.member WHERE MobilePhone LIKE"136%"'
        # sql = "select max(mobilephone) from future.member"
        self.max = self.mysql.fetch_one(sql)
        self.max_mobile = int(self.max)+1
        print(self.max_mobile)

    @classmethod
    def setUpClass(cls):
        cls.request = Request()  # 它是一次会话，会把每次请求的cookie保存起来
        cls.mysql = MysqlUntil()

    @data(*cases)
    def test_register(self,item):
        print("开始执行第{}用例".format(item.id))
        #excel里面是json格式的字符串，把json传成字典
        data_dict = json.loads(item.data)  # Excel字符串转成字典
        if data_dict['mobilephone'] == '${register_mobile}':# 判断是否等于标记
            data_dict['mobilephone'] =  self.max_mobile  # 将最大手机号码+1 赋值给mobilephone
            print(data_dict)
        resp = self.request.request(item.method,item.url,data_dict) # 这里注意要传做过特换的字典！！！！
        print(resp.text)
        try:
            self.assertEqual(item.expected,resp.text,'register error')
            self.do_excel.write_result('register',item.id+1,resp.text,'PASS')
            print("第{}用例执行结果：PASS".format(item.id))
        except AssertionError as e:
            self.do_excel.write_result('register',item.id+1,resp.text,'FAIL')
            print("第{}用例执行结果：FAIL".format(item.id))
            raise e

    def tearDown(self):
       print("用例执行结束")

    @classmethod
    def tearDownClass(cls):
        cls.mysql.close()
        cls.request.session.close()  # 用完记得关闭session



