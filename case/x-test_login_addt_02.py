from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
import ddt

'''
1：输入admin，输入123456，登录
2：输入admin，输入        登录
3：输入qqq，输入123456  ，登录
4：忘记密码
'''

testdatas = [
    {"user":"admin","pwd":"123456","expect":"True"},
    {"user":"admin","pwd":"","expect":"False"},
    {"user":"admin123","pwd":"123456","expect":"False"}
    ]
print(testdatas)

@ddt.ddt
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

    def login_case(self,user,pwd,expect):
        self.login_step.login(user,pwd,)
        result = self.login_step.get_login_result(user)
        print("测试结果：%s"%result)
        self.assertTrue(result == expect)
    @ddt.data(*testdatas)
    def test_(self,data): # 执行三条用例
        '''输入账号admin，输入密码123456，登录,验证结果'''
        # data = testdatas[0]
        print("-------01测试数据：%s--------"%data)
        self.login_case(data["user"],data["pwd"],data["expect"])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()


