from Base.Base import Base
from Page.UIElements import UIElements


class LoginPage(Base):
    """登录页面"""
    def __init__(self, driver):
        Base.__init__(self, driver)

    def login(self, name, passwd):
        """
        登录
        :param name: 用户名
        :param passwd: 密码
        :return:
        """
        # 输入用户名
        self.send_element(UIElements.login_account_id, name)
        # 输入密码
        self.send_element(UIElements.login_passwd_id, passwd)
        # 点击登录
        self.click_element(UIElements.login_btn_id)

    def close_login_page(self):
        """关闭窗口"""
        self.click_element(UIElements.close_login_btn_id)


    def if_login_btn(self):
        # 判断登录按钮是否存在
        self.get_element(UIElements.login_btn_id)