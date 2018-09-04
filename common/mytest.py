#coding=utf-8

import unittest,time
from common import pyselenium
from config import globalparam
from common.log import Log
from common.cmd import cmd
# from common.GetYaml import get_yaml,get_value
from common.error import CustomError

class MyTest(unittest.TestCase):
    """
    The base class is for all testcase.
    """
    @classmethod
    def setUpClass(cls):
        # location = get_yaml("unlog_index", "locators")
        cls.logger = Log()
        cls.logger.info('############################### START ###############################')
        #判断小助手是否启动
        ret = cmd("tasklist").read()
        if "hawkeye" not in ret:
            raise CustomError("小助手未启动，请手动开启")


        cls.dr = pyselenium.PySelenium(globalparam.browser)
        # cls.dr.option()
        cls.dr.max_window()

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
        cls.logger.info('###############################  End  ###############################')
