import logging
import logging.handlers
from common import contants
from common.config import ReadConfig
#输出到文件，文件路径请使用绝对路径 logs
#输出到控制台，定义输出级别是DEBUG
#不同的输出级别可配置
#并不是所有的封装都需要用类进行封装，类是具体相同的行为和特征才需要用类来进行封装
# 日志里级别有哪几种
# debug info warning error critical
config = ReadConfig()
def get_logger(logger_name):
    logger = logging.getLogger(logger_name)  # 创建一个日志收集器
    in_level = config.get('log','in_level')  #总开关直接设置为最低级别（收集的时候）
    logger.setLevel(in_level) # 设置日志级别,给这个日志收集器setLevel（可放配置文件配置）
    #定义日志输出格式
    # fmt = '%(asctime)s-[%(levelname)s]-%(filename)s[line:%(lineno)d] -[%(name)s]-[日志信息]:%(message)s'
    fmt = config.get("log","fmt")
    format = logging.Formatter(fmt) #定义日志的输出格式
        # a ="%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"
    # 输出到指定的文件
    file_name = contants.log_dir
    file_handler = logging.handlers.RotatingFileHandler(file_name,maxBytes=20*1024*1024, backupCount=10, encoding='utf-8')
    file_level = config.get('log','file_level')#输出到文件要考虑资源的占用，所以可以设置级别高一点
    file_handler.setLevel(file_level)   #设置文件输出级别（可进行配置化）
    file_handler.setFormatter(format)  # 设置文件输出格式

    #输出到控制台
    console_handler = logging.StreamHandler()
    console_level = config.get('log','console_level')
    console_handler.setLevel(console_level)
    console_handler.setFormatter(format)

    # 日志收集器与输出渠道进行对接
    logger.addHandler(file_handler) #输出到文件
    logger.addHandler(console_handler)#输出到控制台

    return logger

if __name__ == '__main__':
    log = get_logger(logger_name='invest')
    log.error("this is error")
    log.debug("this is debug")
