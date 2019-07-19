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
        sql = 'SELECT max(MobilePhone) as max_phone FROM future.member WHERE MobilePhone LIKE"136%"'
        # sql = "select max(mobilephone) from future.member"
        self.max = self.mysql.fetch_one(sql)["max_phone"]
        self.max_mobile = int(self.max)+1
        print(self.max_mobile)

    @classmethod
    def setUpClass(cls):
        cls.request = Request()  # 它是一次会话，会把每次请求的cookie保存起来
        cls.mysql = MysqlUntil(return_dacit=True)

    @data(*cases)
    def test_register(self,item):
        print("开始执行第{}用例".format(item.id))
        #excel里面是json格式的字符串，把json传成字典
        data_dict = json.loads(item.data)  # Excel字符串转成字典
        if data_dict['mobilephone'] == '${register_mobile}':# 判断是否等于标记
            data_dict['mobilephone'] =  self.max_mobile # 将最大手机号码+1 赋值给mobilephone
            print(data_dict)
        resp = self.request.request(item.method,item.url,data_dict) # 这里注意要传做过特换的字典！！！！
        print(resp.text)
        try:
            self.assertEqual(item.expected,resp.text,'register error')
            if resp.json()['msg'] == "注册成功":
                sql = "select * from future.member where mobilephone = {0}".format(data_dict['mobilephone'])
                results = self.mysql.fetch_all(sql)
                #首先判断是否有成功插入数据，判断列表的长度
                self.assertEqual(1,len(results))
                #判断余额
                member = results[0]#获取到这一条数据，是一个字典
                # print(member['LeaveAmount'], type(member['LeaveAmount']))
                # print(type(member))
                self.assertEqual(0,member['LeaveAmount'])#注意与表的列表是一致的，判断注册成功余额应该是0
                #判断注册用户的类型是1
                self.assertEqual(1,member['Type'])
                #判断密码是否加密
                self.assertNotEqual(data_dict['pwd'],member['Pwd'])
                #没有写用户名的话，默认的注册名应该是小蜜蜂
                if 'regname' in data_dict.keys():
                    self.assertEqual(data_dict['regname'], member['RegName'])
                else:
                    self.assertEqual("小蜜蜂",member['RegName'])


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

