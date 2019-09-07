# coding = utf-8
from selenium import webdriver
import time
import unittest

class LoginTest(unittest.TestCase):
    '''登录类的案例'''
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()

    def setUp(self):
        self.driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
        self.is_alert_exist()
        self.driver.delete_all_cookies()
        self.driver.refresh()


    def get_login_username(self):
        try:
            t = self.driver.find_element_by_css_selector("#userMenu>a").text
            return t
        except:
            return ""

    def is_alert_exist(self):
        try:
            time.sleep(2)
            alert = self.driver.switch_to.alert
            text = alert.text
            alert.accept()
            return text
        except:
            return " "

    def login(self,user,pwd):
        self.driver.find_element_by_id("account").send_keys(user)
        self.driver.find_element_by_name("password").send_keys(pwd)
        self.driver.find_element_by_id("submit").click()
    def test_01(self):
        '''登录成功案例'''
        time.sleep(2)
        # 正确的账号密码
        self.login("admin","123456")

        #判断是否登录成功
        time.sleep(2)
        t = self.get_login_username()
        print("获取的结果：%s"%t)
        self.assertTrue(t == "admin")

    # def test_02(self):
    #     '''登录失败案例'''
    #     time.sleep(2)
    #     # 错误的账号密码
    #     self.login("admin","admin1")
    #     #判断是否登录成功
    #     time.sleep(2)
    #     t = self.get_login_username()
    #     print("登陆失败，获取结果%s"%t)
    #     self.assertTrue(t == 2) # 断言失败截图
    #     time.sleep(3)

    # 截图为空时
    # def tearDown(self):
    #     self.is_alert_exist()
    #     self.driver.delete_all_cookies()
    #     self.driver.refresh()

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

#以脚本运行
if __name__ == "__main__":
    # 用例执行不需要实例化 if __name__ 下写个unittest.main()就行了，不要搞复杂了
    unittest.main()