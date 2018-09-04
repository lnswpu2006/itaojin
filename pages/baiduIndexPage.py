#coding=utf-8

from common import basepage
from common import GetYaml
data = GetYaml.parseyaml()
class BaiduIndexPage(basepage.Page):


    def into_index_page(self):
        """打开t.itaojin首页"""
        self.dr.open('t.itaojin.cn')
    def login(self):
        """进行登录操作"""
        self.dr.click(data)
        self.dr.clear_type('id->kw',values)

    def click_search_button(self):
        """点击搜索按钮"""
        self.dr.click('id->su')

    def return_title(self):
        """返回该页面的title"""
        return self.dr.get_title()