import os, sys

import pytest
from selenium.common.exceptions import TimeoutException

sys.path.append(os.getcwd())
import time

from Base.getDriver import get_phone_driver
from Page.page import Page
from Base.getfiledata import GetFileData


def get_login_data():
    # 成功列表
    suc_list = []
    # 预期错误列表
    fail_list = []
    # 读取yaml文件数据
    data = GetFileData().get_yaml_data("logindata.yml")
    for i in data:
        if data.get(i).get("toast"):
            fail_list.append((i, data.get(i).get("account"),
                              data.get(i).get("passwd"),
                              data.get(i).get("toast"),
                              data.get(i).get("expect_data")))
        else:
            suc_list.append((i, data.get(i).get("account"),
                             data.get(i).get("passwd"),
                             data.get(i).get("expect_data")))
    return {"suc": suc_list, "fail": fail_list}


class TestLogin:
    def setup_class(self):
        self.driver = get_phone_driver("com.yunmall.lc", "com.yunmall.ymctoc.ui.activity.MainActivity")
        self.page_obj = Page(self.driver)

    def teardown_class(self):
        time.sleep(10)
        self.driver.quit()

    @pytest.fixture(autouse=True)
    def auto_login(self):
        # 点击我
        self.page_obj.get_homepage().click_my_btn()
        # 点击已有账号
        self.page_obj.get_signpage().click_exits_account()

    @pytest.mark.parametrize("test_num,account,passwd,expect", get_login_data().get("suc"))
    def test_suc_login(self, test_num, account, passwd, expect):
        # 登录操作 --个人中心
        self.page_obj.get_loginpage().login(account, passwd)

        # 捕获异常
        try:
            # 获取我的优惠的文本信息
            my_discount = self.page_obj.get_personpage().get_shop_cart()
            # 捕获 断言结果异常
            try:
                # 断言
                assert expect == my_discount
            # 出现AssertionError 之后的操作
            except AssertionError:
                """停留在个人中心,需要执行退出操作"""
                # 截图
                self.page_obj.get_loginpage().screen_page()
                # 断言失败
                assert False
            # 不管是否出现异常 都需要
            finally:
                # 点击设置
                self.page_obj.get_personpage().click_setting_btn()
                # 退出操作
                self.page_obj.get_settingpage().logout()
        # 异常操作
        except TimeoutException:
            """停留在登录页面"""
            # 截图
            self.page_obj.get_personpage().screen_page()
            # 关闭登录窗口
            self.page_obj.get_loginpage().close_login_page()
            # 断言失败
            assert False

    @pytest.mark.parametrize(" test_num, account, passwd, toast, expect",get_login_data().get("fail"))
    def test_login_fail(self, test_num, account, passwd, toast, expect):
        # 登录操作 --个人中心
        self.page_obj.get_loginpage().login(account, passwd)
        try:
            # 获取toast消息
            toast_data = self.page_obj.get_settingpage().get_toast(toast)
            try:
                """登录页面操作"""
                # 判断登录按钮是否存在
                self.page_obj.get_loginpage().if_login_btn()
                # 断言
                assert toast_data == expect
                # 关闭登录页面
                self.page_obj.get_loginpage().close_login_page()

            except TimeoutException:
                """获取到toast错误信息,但登录成功"""
                # 截图
                self.page_obj.get_loginpage().screen_page()
                # 点击设置
                self.page_obj.get_personpage().click_setting_btn()
                # 退出操作
                self.page_obj.get_settingpage().logout()
                assert False

            except AssertionError:
                """登录页面"""
                # 截图
                self.page_obj.get_settingpage().screen_page()
                # 关闭登录窗口
                self.page_obj.get_loginpage().close_login_page()
                assert False

        except TimeoutException:
            # 棘突
            self.page_obj.get_settingpage().screen_page()
            # 找不到toast
            try:
                """登录页面"""
                # 登录按钮
                self.page_obj.get_loginpage().if_login_btn()
                # 关闭登录页面
                self.page_obj.get_loginpage().close_login_page()
            except TimeoutException:
                """个人中心页面"""
                # 点击设置
                self.page_obj.get_personpage().click_setting_btn()
                # 退出操作
                self.page_obj.get_settingpage().logout()

            assert False
