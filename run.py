#coding=utf-8

import unittest
# import
from BeautifulReport import BeautifulReport
import time
from config import globalparam
from common import sendmail

def run():
    test_dir = './testcase'
    print(test_dir)
    suite = unittest.defaultTestLoader.discover(start_dir=test_dir,pattern='test*.py')

    now = time.strftime('%Y-%m-%d_%H_%M_%S')
    reportname = 'TestResult' + now + '.html'
    print(reportname)
    # with open(reportname,'wb') as f:
    #     runner = HTMLTestRunner.HTMLTestRunner(
    #         stream=f,
    #         title='测试报告',
    #         description='Test the import testcase'
    #     )
    #     runner.run(suite)
    BeautifulReport(suite).report(filename=reportname,description='测试报告',log_path=globalparam.report_path)
    time.sleep(3)
    # 发送邮件
    # mail = sendmail.SendMail()
    # mail.send()

if __name__=='__main__':
    run()
