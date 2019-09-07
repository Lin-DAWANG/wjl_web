from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url

'''
1：输入admin，输入123456，登录
2：输入admin，输入        登录
3：输入admin，输入123456，记住密码，登录
4：忘记密码
'''
class LoginPageCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.login_step = LoginPage(cls.driver)

    def setUp(self):
        self.driver.get(login_url)
        self.login_step.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()

    def test_01(self):
        '''输入账号admin，输入密码123456，登录,验证结果'''
        self.login_step.input_user("admin")
        self.login_step.input_pwd("123456")
        self.login_step.click_submit()
        result = self.login_step.get_login_name()
        self.assertTrue(result == "admin")


    def test_02(self):
        '''输入账号admin，不输入密码，登录,验证结果'''
        self.login_step.input_user("admin")
        self.login_step.input_pwd()
        self.login_step.click_submit()
        result = self.login_step.get_login_name()
        self.assertTrue(result == "")

    def test_03(self):
        '''输入账号admin，输入密码123456，记住密码登录,验证结果'''
        self.login_step.input_user("admin")
        self.login_step.input_pwd("123456")
        self.login_step.click_keep_login()
        self.login_step.click_submit()
        result = self.login_step.get_login_name()
        self.assertTrue(result == "admin")

    def test_04(self):
        '''忘记密码'''
        self.login_step.click_forget_psw()
        result = self.login_step.is_forgrt_page_exist()
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()


