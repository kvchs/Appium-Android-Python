import logging
import logging.config

# 读取配置文件log.conf生成log规格
# CON_LOG = 'log.conf'
# logging.config.fileConfig(CON_LOG)
# logging2 = logging.getLogger()
# logging2.info("test log file")

# logging.basicConfig(level=logging.DEBUG, filename='runlog.log', filemode='w')
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s --> %(message)s')
logging.debug("debug info")
logging.info('info level')
logging.warning('warning info')
logging.error('error info')
logging.critical('critical info')

