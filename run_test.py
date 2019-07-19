import unittest
from libext import HTMLTestRunnerNew

from common import contants
#自动查找testcase目录下，以test开头的.py文件里面的测试类
discover = unittest.defaultTestLoader.discover(contants.testcases_dir,pattern="test_*.py",top_level_dir=None)

with open(contants.reports_html,"wb+") as file:
    runner = HTMLTestRunnerNew.HTMLTestRunner(stream=file,
                                              verbosity=2,
                                              title="api",
                                              description="前程贷接口测试报告",
                                              tester="李艳荷")
    runner.run(discover)#执行查找到的测试用例