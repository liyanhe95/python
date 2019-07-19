import pymysql
from common.config import ReadConfig
class MysqlUntil:
    #定义MySQL的操作类，mysql经常进行的操作，把这些操作都定义为它的方法
    #建立一次数据库连接，建立一个查询，做完所有的操作之后再关闭
    def __init__(self,return_dacit=False):
        #建立数据库连接
        # host = "test.lemonban.com"
        # user = "test"
        # password = "test"
        config = ReadConfig()
        host = config.get("database", "host")
        user = config.get("database","user")
        password = config.get("database","password")
        self.mysql = pymysql.connect(host=host, user=user, password=password, port=3306)
        # 新建一个查询页面
        if return_dacit:
            self.cursor = self.mysql.cursor(pymysql.cursors.DictCursor)#指定每行数据以字典的形式返回
        else:
            self.cursor = self.mysql.cursor()#指定每行数据以元组的形式返回


    def fetch_one(self,sql):
        #执行sql
        self.cursor.execute(sql)
        #查看结果
        self.mysql.commit()#使用同一个实例进行多次查询时，每次执行完commit一下，更新查询
        result = self.cursor.fetchone()  # 返回最近的一条,返回的是元组
        return result  # 返回的是元组，所以使用索引取值，通过下标取值可读性比较差

    def fetch_all(self,sql):
        #执行sql
        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results   #返回的是列表[(),(),()],里面存放的是元组


    def close(self):
        # 关闭查询
        self.cursor.close()
        #关闭数据库连接
        self.mysql.close()


if __name__ == '__main__':
    # mysql = MysqlUntil()
    # sql = "select max(mobilephone) from future.member"
    # result = mysql.fetch_one(sql)
    # print(result)
    # mysql.close()
    mysql = MysqlUntil(return_dacit=True)
    sql = "select * from future.member limit 10"
    results = mysql.fetch_all(sql)#返回的是列表里面存放字典
    for result in results:
        print(result["Id"])
    mysql.close()