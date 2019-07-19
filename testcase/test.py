from common import contants
from common.request import Request
from common.do_excel import DoExcel

#请求不成功
#url data text json
#str--->dict eval  json loads
#接口自动化的流程   写用例---执行用例---报告
#unittest
#case  测试用例
#suite 测试套件
#loader 加载测试用例
#run 执行测试用例
#result 测试结果  测试报告
#main（程序的入口）  收集当前模块的unittest的用例
#mock  模拟测试
#TestCase   setUP tearDown run assertEqual
#TestLoader loadTestFromModule  loadTestFromName
#TestSuite addTest addTests run
#HTMLTestRunnerNew
do_excel = DoExcel(contants.case_file)
rest = do_excel.get_data('login')

request = Request()  # 实例化对象
for item in rest:
    print("开始执行第{}用例".format(item.id))  # 从excel里面读出来的数据是一个个的字符串，所以需要转换
    #使用封装好的request 来完成请求
    resp = request.request(item.method, item.url, item.data)
    #将返回结果和期望结果进行匹配
    if resp.text == item.expected:
        #一致就写入excel的结果为PASS，
        do_excel.write_result('login', item.id + 1, resp.text, 'PASS')# item.id+1是当前的row，resp.text真实值
        print("第{}用例执行结果：PASS".format(item.id))
    else:
        do_excel.write_result('login', item.id + 1, resp.text, 'FAIL')
        print("第{}用例执行结果：FAIL".format(item.id))