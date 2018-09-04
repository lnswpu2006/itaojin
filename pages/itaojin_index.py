from common import basepage
from common.GetYaml import get_value

class ItaojinIndexPage(basepage.Page):
    def into_itaojin_index_page(self):
        '''打开t.itaojin.cn首页'''
        self.dr.open("http://t.itaojin.cn")
    def login_from_index(self):
        '''首页用户名账号登录,并返回登陆后的标题'''
        self.dr.click(get_value("login"))
        self.dr.click(get_value('login_by_username'))
        self.dr.clear_type(get_value("username"), '1398089145011')#这里的账号密码后面需要进行参数化或者配置
        self.dr.clear_type(get_value("password"), '123456')
        self.dr.click(get_value('submit'))

    def title(self):
        '''返回title'''
        self.dr.get_title()


