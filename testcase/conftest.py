#-*-coding:utf-8-*-
# @time      :2019/1/2014:46
# @Author   :lemon_hehe
# @Email     :976621712@qq.com
# @File      :test_login.py
# @software:PyCharm Community Edition
#conftest 是固定的格式，不可以改的。pytest只要建立了这样的一个文件，它就在这个文件里面来找
#根本不需要导入，直接使用usefixtures,它就会自己去找fixture
#我们的环境不是用来和测试用来绑定的
import pytest
from common.request import Request
from common.mysql import MysqlUntil

#return可以终止一个函数，而yield可以接着执行
@pytest.fixture('class')
#可以实现setupclass
def my_set_class():
    #只会在某个类里面去执行一次
    request = Request()
    mysql = MysqlUntil(return_dacit=True)
    yield (request,mysql)

    print('finish my class')
    request.session.close()  # 用完记得关闭session
    mysql.close()  # 关闭数据库 mysql

