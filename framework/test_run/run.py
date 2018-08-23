import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('.'))))
import logging
import time
import unittest

# from HtmlTestRunner import HTMLTestRunner
from framework.config.HTMLTestReportCN import HTMLTestRunner

# sys.path.append(os.path.dirname(os.path.abspath('.')))
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath('.'))))
test_dir = '../test_case'
report_dir = '../reports'

discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_login.py')
now = time.strftime('%Y-%m-%d %H-%M-%S')
report_name = report_dir + '/' + now + ' test_report.html'
with open(report_name, 'wb') as file:
    runner = HTMLTestRunner(title='test login report', description='test description', stream=file)
    logging.info('run test case with HTMLTestRunner')
    runner.run(discover)