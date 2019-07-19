#不变的是常量
#无论在哪用都可以直接contants.
import os
# 项目地址
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  #项目根路径
# print(base_dir)
# datas 目录地址
data_dir = os.path.join(base_dir,"datas")#拼接路径  找到data文件夹
case_file = os.path.join(data_dir,"test.xlsx") #拼接路径  在datas下面再去找test.xlsx文件
# print(case_file)
data_json = os.path.join(data_dir,'data.json')
# print(data_json)
conf_dir = os.path.join(base_dir,"conf")
test_conf = os.path.join(conf_dir,"test.conf")#测试配置文件路径
test2_conf = os.path.join(conf_dir,"test2.conf")
global_conf = os.path.join(conf_dir,"global.conf")
# print(test_conf)
# print(test2_conf)
# print(global_conf)
#log地址
log = os.path.join(base_dir,"log")
log_dir = os.path.join(log,"case.log")
# print(log_dir)

testcases_dir = os.path.join(base_dir,"testcase")
# print(testcases_dir)

reports_dir = os.path.join(base_dir,"reports")
# print(reports_dir)
reports_html = os.path.join(reports_dir,"reports.html")

sql_dir = os.path.join(base_dir,"sql_data")
withdraw_dir = os.path.join(sql_dir,'withdraw.text')
money_dir = os.path.join(sql_dir,"money.text")
# print(money_dir)
recharge_dir = os.path.join(sql_dir,"recharge.text")
recharge_money = os.path.join(sql_dir,"recharge_money.text")
invest_dir = os.path.join(sql_dir,"invest.text")
invest_result = os.path.join(sql_dir,"invest_result.text")