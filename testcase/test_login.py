import time
from common import mytest
from pages import itaojin_index
from common.GetYaml import get_value,get_yaml
from common.error import CustomError


class Test_itaojin(mytest.MyTest):
    '''首页用户账号登录'''

    def login(self):
        '''
        测试登录
        '''
        location = get_yaml("unlog_index")
        # self.dr.option()

        self.dr.open("http://t.itaojin.cn")
        self.dr.click(get_value(location,"登录"))
        self.dr.click(get_value(location,'login_by_username'))
        self.dr.clear_type(get_value(location,"username"), '1398089145011')#这里以后需要进行参数化或者配置
        self.dr.clear_type(get_value(location,"password"), '123456')
        self.dr.click(get_value(location,'submit'))
        time.sleep(5)
        title = self.dr.get_title()
        # print(title)
        self.assertIn("首页",title)
        self.dr.switch_default()
        self.dr.current_window()
        for i in range(15):

            value= self.dr.get_attribute("css->body > div.modal.fade.in > div > div > div.modal-body > form > div.btn-box > input","value")
            print(value)
            time.sleep(1)
            if value == "同意":
                self.dr.click("css->body > div.modal.fade.in > div > div > div.modal-body > form > div.btn-box > input")
                break

    def test_1_login(self):
        '''
        用户登录
        :return:
        '''
        self.login()

    def test_2_workcenter(self):
        '''
        跳转到任务中心
        :return:
        '''
        index_locations = get_yaml("log_index")
        # self.dr.click(get_value(index_locations,"任务中心"))
        time.sleep(3)
        self.dr.open_new_window(get_value(index_locations,"任务中心"))
        title = self.dr.get_title()
        self.assertIn("任务中心",title)
        bench_locations = get_yaml("workbench")
        # for bench_location in bench_locations:
        #     print(self.dr.get_text(bench_location["css"]))
        self.dr.element_wait(get_value(bench_locations,"图表"),10)
    def test_3_call(self):
        '''通话模块'''
        call_locations = get_yaml("call")
        try:

            self.dr.click(get_value(call_locations,"通话"))
            self.dr.element_wait(get_value(call_locations,"所有通话"),10)
        except:
            raise CustomError("规定时间内未跳转到通话模块")

        # for call_location in call_locations:
        #     print(self.dr.get_text(call_location["css"]))
        #获取商家，并分别点击
        stores = self.dr.get_elements(get_value(call_locations,"商家汇总"))
        for store in stores:
            print(store.text)
            store.click()
            print("*******")
            time.sleep(1)




