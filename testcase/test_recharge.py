import unittest
import json
from ddt import ddt,data
from common import contants
from common import context
from common.request import Request
from common.do_excel import DoExcel
from common.mysql import MysqlUntil
#1.excel 里面设计第一条case是正常登录
#2.session保持会话的方式来进行请求的话，那就需要把request实例化对象放到类里面
#3.获取数据，运行用例

##用session去做cookie的转递
#第一条用例中有没有cookie的返回，如果有的话就把它带进去，cookie的明文转递

@ddt
class RechargeTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_data('recharge')

    def setUp(self): #重写了父类unittest.TestCase里面的setUP
        #每个测试方法里面去运行的操作
        pass

    @classmethod  #类方法是整个类只会运行一次
    def setUpClass(cls):
        #cls 代表的是类名  类的本身
        # 每个测试类里面去运行的操作放到类方法里面
        #cls.request 设置一个类变量
        cls.request = Request()  # 实例化对象，建立一个session会话
        cls.mysql = MysqlUntil(return_dacit=True)

    @data(*cases)
    def test_recharge(self,item):
        #self  是实例的一个引用
        print("开始执行第{}用例".format(item.id))
        #self.request是实例变量
        #self是RechargeTest的一个实例
        data_new = context.replace_new(item.data)
        resp = self.request.request(item.method,item.url,data_new)
        # resp.__dict__
        try:
            self.assertEqual(str(item.expected),str(resp.json()['code']),"recharge error")
            if resp.json()["msg"] == "登录成功":
                sql = "select * from future.member where mobilephone = {0}".format(json.loads(data_new)['mobilephone'])
                results = self.mysql.fetch_all(sql)
                member = results[0]
                with open(contants.recharge_dir, "w") as file:#登陆成功后，获取到最初的leavemount值，然后写入member初始leaveamount的值
                    file.write(str(member['LeaveAmount']))

            if resp.json()["msg"] == "充值成功":
                # sql2 = "select * from future.member where mobilephone = {0}".format(json.loads(data_new)['mobilephone'])
                # results2 = self.mysql.fetch_all(sql2)
                # member2 = results2[0]
                # updated_recharge = member2['LeaveAmount']  # 充值成功后获取最新的leaveamount值
                with open(contants.recharge_dir,"r") as r: #读取写入text中最初的leaveamount的值
                    read_recharge = r.read()

                import decimal
                read_recharge_decimal = decimal.Decimal(read_recharge)
                setup_amount = json.loads(data_new)['amount']
                setup_amount_decimal = decimal.Decimal(setup_amount)
                money = read_recharge_decimal - setup_amount_decimal
                with open(contants.recharge_money,"w") as w:
                    w.write(str(money))

                with open(contants.recharge_money,"r") as r:
                    read_money = r.read()
                read_money_decimal = decimal.Decimal(read_money)
                self.assertEqual(read_money_decimal,money)


            self.do_excel.write_result('recharge',item.id+1,resp.text,'PASS')
            print("第{}用例执行结果：PASS".format(item.id))
        except AssertionError as e:
            self.do_excel.write_result('recharge',item.id+1,resp.text,'FAIL')
            print("第{}用例执行结果：FAIL".format(item.id))
            raise e

    def tearDown(self):
        pass

    @classmethod
    def tearDownClass(cls):
        cls.request.close()  # 用完记得关闭session
        cls.mysql.close()