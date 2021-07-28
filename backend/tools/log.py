

import logging
from logging.handlers import RotatingFileHandler
import os,sys
import datetime

#如果用pyinstaller打包成exe 再运行，容易报找不到路径，下面是替代方式，
# 但用 pyinstaller -D xx.py 解决了这个问题，可继续使用
#如果是 pyinstaller -F xx.py 注意参数 --runtime-tmpdir 但没有研究透
abspath = os.path.abspath(__file__)  

#abspath = os.path.realpath(sys.executable) 这个默认会是python路径，也不中
#abspath = os.path.realpath(sys.argv[0]) #改成执行时的参数输入
BASE_PATH = os.path.dirname(os.path.dirname(abspath))

LOGGER_ROOT_NAME = 'chineseocr-lite-onnx'
logger = logging.getLogger(LOGGER_ROOT_NAME)
logger.setLevel(logging.INFO)
# Formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - [%(levelname)s] | %(message)s',
                              datefmt='%Y/%m/%d %H:%M:%S')

logfile_name = datetime.date.today().__format__('%Y-%m-%d.log')
logfile_path = os.path.join(BASE_PATH, f'logs/')
if not os.path.exists(logfile_path):
    os.mkdir(logfile_path)

handler_logfile = RotatingFileHandler(logfile_path + logfile_name,
                                      maxBytes=1 * 1024 * 1024,
                                      backupCount=3)
handler_logfile.setLevel(logging.INFO)
handler_logfile.setFormatter(formatter)

console_output = logging.StreamHandler()
console_output.setLevel(logging.INFO)
console_output.setFormatter(formatter)

logger.addHandler(handler_logfile)
logger.addHandler(console_output)
