# import openpyxl
# #
# # class Case:
# #     def __init__(self):
# #         self.case_id = None
# #         self.title = None
# #         self.url = None
# #         self.data = None
# #         self.method = None
# #         self.expected = None
# #         self.actual = None
# #         self.result = None
# #
# # class DoExcel:
# #
# #     def __init__(self,file_name):
# #         try:
# #             self.fil_ename = file_name
# #             self.workbook = openpyxl.load_workbook(filename=file_name)
# #         except FileNotFoundError as e:
# #             print('{0} not fund,please check file path'.format(file_name))
# #             raise e
# #
# #     def get_cases(self,sheet_name):
# #         sheet_name = sheet_name
# #         sheet = self.workbook[sheet_name]
# #         max_row = sheet.max_row
# #         cases = []
# #         for r in range(2,max_row + 1):
# #             case = Case()
# #             case.id = sheet.cell(row=r,column=1).value
# #             case.title = sheet.cell(row=r,column=2).value
# #             case.url = sheet.cell(row=r,column=3).value
# #             case.data = sheet.cell(row=r,column=4).value
# #             case.method = sheet.cell(row=r,column=5).value
# #             case.expected = sheet.cell(row=r,column=6).value
# #             if type(case.expected) == int:
# #                 case.expected = str(case.expected)
# #             cases.append(case)#将cases 放到case列表里面
# #
# #         return cases #for循环结束后返回cases列表
# #
# #     def write_result(self,sheet_name,row,actual,result):
# #         sheet = self.workbook[sheet_name] #读取文件中的sheet_name
# #         sheet.ceel(row,7).value = actual  #写入实际结果
# #         sheet.ceel(row,8).value = result  #写入执行结果
# #         self.workbook.save(filename=self.fil_ename)  #保存文件
# #
# # if __name__ == '__main__':
# #     from common import contants
# #     from common.request import Request
# #     do_excel = DoExcel(contants.case_file)
# #     cases = do_excel.get_cases('login')  #执行这个测试用例 然后返回到cases 列表中
# #     print(cases)
# #     request = Request() #实例化一个request对象
# #
# #     for case in cases:
# #         resp = request.request(case.method,case.url,case.data)
# #         print(resp.json())
# #
# #         if resp.text ==case.expected:
# #             do_excel.write_result(case.id+1,resp.text,'PASS')
# #         else:
# #             do_excel.write_result(case.id+1,resp.text,'FAIL')



import pytest

class TestLogin():

    def setup_class(self):
        print('开始测试环境')

    def test_add(self):
        print("tong")

if __name__ == '__main__':
    pytest.main(['-s','-q','1.py'])






