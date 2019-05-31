from Page.homepage import HomePage
from Page.signpage import SignPage
from Page.loginpage import LoginPage
from Page.personpage import PersonPage
from Page.settingpage import SettingPage

class Page:
    def __init__(self,driver):
        self.driver = driver
    def get_homepage(self):
        """返回首页页面对象"""
        return HomePage(self.driver)

    def get_signpage(self):
        """返回注册页面对象"""
        return SignPage(self.driver)

    def get_loginpage(self):
        """获取登录页面对象"""
        return LoginPage(self.driver)

    def get_personpage(self):
        """获取个人中心页面"""
        return PersonPage(self.driver)

    def get_settingpage(self):
        return SettingPage(self.driver)