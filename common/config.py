# ConfigParser配置类  专门来读取配置文件的
# 配置文件：结尾以 .ini、.conf、 .config 、.properties、xml

# 配置文件一般是什么样的

# section 片段/区域 [区域名]
# option 相当于字典里面的key，一个个配置的选项
# value  相当于字典里面的value
import configparser
from common import contants

class ReadConfig:
    # 读取配置文件类，解析配置文件
    def __init__(self):
        # 只要实例化ReadConfig对象时它都会自动去调用
        # 1 实例化对象
        # self.config 实例化变量，方便后面调用
        self.config = configparser.ConfigParser()
        # 2 加载文件
        self.config.read(contants.global_conf)  # 先加载开关的配置
        open = self.config.getboolean("switch", "open")

        if open:
            self.config.read(contants.test_conf,encoding="utf-8")  # open是True
        else:
            self.config.read(contants.test2_conf,encoding="utf-8")  # open是false

    def get(self, section, option):  # 因为里面的方法需要传参，所以也需要外面的方法给我传进来参数
        # 做了这一层封装就是统一了config的入口，不需要去操作里面的config
        try:
            return self.config.get(section, option)
        except  Exception as e:
            print('The configuration file is loaded correctly')
            raise e

    def getboolean(self, section, option):
        try:
            return self.config.getboolean(section, option)
        except Exception as e:
            print('The configuration file is loaded correctly')
            raise e

    def get_int(self, section, option):
        try:
            return self.config.getint(section, option)
        except Exception as e:
            print('The configuration file is loaded correctly')
            raise e

    def get_float(self, section, option):
        try:
            return self.config.getfloat(section, option)
        except Exception as e:
            print('The configuration file is loaded correctly')
            raise e


if __name__ == '__main__':
    config = ReadConfig()
    value = config.get("api", "pre_url")
    print(value)
