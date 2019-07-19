#使用python连接数据库，需要使用  pip install pymysql

import pymysql
#1  建立数据库连接
host = "test.lemonban.com"
user = "test"
password = "test"
mysql = pymysql.connect(host=host, user=user, password=password, port=3306)
#2  新建一个查询页面
cursor = mysql.cursor()
#3  编写sql
sql = "select max(mobilephone) from future.member"
#4  执行sql
cursor.execute(sql)
#5  查看结果
result = cursor.fetchone() #返回最近的一条,返回的是元组
print(result[0])#返回的是元组，所以使用索引取值
#6  关闭查询
cursor.close()
#7  关闭数据库连接
mysql.close()