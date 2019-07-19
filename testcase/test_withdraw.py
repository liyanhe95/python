import unittest
import json
from common import context
from common import contants
from libext.ddtnew import ddt,data
from common.request import Request
from common.do_excel import DoExcel
from common.mysql import MysqlUntil

@ddt
class TestWithdraw(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_data("withdraw")

    @classmethod
    def setUpClass(cls):
        cls.request = Request()
        cls.mysql = MysqlUntil(return_dacit=True)

    @data(*cases)
    def test_withdraw(self,item):
        print("开始执行第{}用例".format(item.id))
        data_new = context.replace_new(item.data)
        resp = self.request.request(item.method,item.url,data_new)
        # resp.__dict__
        print(type(item.expected),type(resp.json()['code']))
        try:
            self.assertEqual(str(item.expected),str(resp.json()['code']),"withdraw error")
            if resp.json()['msg'] == "登录成功":#登陆成功后，获取到最初的leavemount值，然后写入member初始leaveamount的值
                sql = "select * from future.member where mobilephone = {0}".format(json.loads(data_new)['mobilephone'])
                results = self.mysql.fetch_all(sql)
                member = results[0]
                with open(contants.withdraw_dir,"w") as file:
                    file.write(str(member['LeaveAmount']))
            if resp.json()['msg'] == "取现成功":
                # sql2 = "select * from future.member where mobilephone = {0}".format(json.loads(data_new)['mobilephone'])
                # results2 = self.mysql.fetch_all(sql2)
                # member2 = results2[0]
                # new_withdraw = member2['LeaveAmount'] # 提现成功后获取最新的leaveamount值
                with open(contants.withdraw_dir,"r") as r: #读取写入text中最初的leaveamount的值
                    read_withdraw = r.read()

                import decimal
                read_withdraw_decimal = decimal.Decimal(read_withdraw)
                setup_amount = json.loads(data_new)['amount']
                setup_amount_decimal = decimal.Decimal(setup_amount)
                money = read_withdraw_decimal - setup_amount_decimal
                with open(contants.money_dir,"w") as w:
                    w.write(str(money))

                with open(contants.money_dir,"r") as r:
                    read_money = r.read()
                read_money_decimal = decimal.Decimal(read_money)
                self.assertEqual(read_money_decimal,money)

            self.do_excel.write_result("withdraw",item.id+1,resp.text,"PASS")
            print("第{}用例执行结果：PASS".format(item.id))
        except AssertionError as e:
            self.do_excel.write_result("withdraw",item.id+1,resp.text,"FAIL")
            print("第{}用例执行结果：FAIL".format(item.id))
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.request.close()#关闭session
        cls.mysql.close()