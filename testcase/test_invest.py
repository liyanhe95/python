import unittest
import json
from ddt import ddt,data
from common import contants
from common.request import Request
from common.do_excel import DoExcel
from common import context
from common.context import Context
from common.mysql import MysqlUntil
@ddt
class InvestTest(unittest.TestCase):
    do_excel = DoExcel(contants.case_file)
    cases = do_excel.get_data("invest")

    @classmethod
    def setUpClass(cls):
        cls.request = Request()
        cls.mysql = MysqlUntil(return_dacit=True)

    @data(*cases)
    def test_invest(self,item):
        print("开始执行第{}用例".format(item.id))
        #查找参数化的测试数据，动态替换
        data_new = context.replace_new(item.data)#str类型的测试数据 ,替换后新的data
        resp = self.request.request(item.method,item.url,data_new)
        print(resp.text)
        try:
            self.assertEqual(str(item.expected),resp.json()['code'],"invest error")
            self.do_excel.write_result('invest', item.id + 1, resp.text, 'PASS')
            print("第{}用例执行结果：PASS".format(item.id))
            #判断是否加标成功，如果成功就按照借款人ID去数据库查询最新记录
            if resp.json()['msg'] == "加标成功":
                loan_member_id = getattr(Context,"loan_member_id")
                sql ="SELECT id from future.loan where MemberID = '{0}' ORDER BY CreateTime desc LIMIT 1".format(loan_member_id)
                loan_id = self.mysql.fetch_one(sql)
                setattr(Context,"loan_id",str(loan_id)) #动态的去添加loan_id,记得转成str，后续通过正则替换，因为正则操作的是str

                if resp.json()["msg"] == "登录成功":
                    sql2 = "select Amount,MemberID from future.invest where MemberID = {0}".format(data_new["memberId"])
                    results = self.mysql.fetch_all(sql2)
                    member_amount = results[0]

                    with open(contants.invest_dir,"w") as file:
                        file.read(str(member_amount["Amount"]))

                    # with open(contants.invest_dir,"r") as r:
                    #     read_amount = r.read()

                if resp.json()["msg"] == "投资成功":
                    # sql2 = "select Amount,MemberID from future.invest where MemberID = {0}".format(data_new["memberId"])
                    # results = self.mysql.fetch_all(sql2)
                    # member_amount = results[0]
                    # with open(contants.invest_dir, "w") as file:
                    #     file.read(str(member_amount["Amount"]))

                    with open(contants.invest_dir,"r") as r:
                        read_amount = r.read()

                    import decimal
                    read_amount_decimal = decimal.Decimal(read_amount)
                    invest_amount = json.loads(data_new)['Amount']
                    invest_amount_decimal = decimal.Decimal(invest_amount)
                    count_amount = read_amount_decimal + invest_amount_decimal
                    with open(contants.invest_result,"w") as w:
                        w.write(str(count_amount))

                    with open(count_amount,"r") as r:
                        read_count_amount = r.read()
                    read_count_amount_decimal = decimal.Decimal(read_count_amount)
                    self.assertEqual(read_count_amount_decimal,count_amount)

        except AssertionError as e:
            self.do_excel.write_result('login', item.id + 1, resp.text, 'FAIL')
            print("第{}用例执行结果：FAIL".format(item.id))
            raise e

    @classmethod
    def tearDownClass(cls):
        cls.request.session.close()  # 用完记得关闭session
        cls.mysql.close() #关闭数据库 mysql



