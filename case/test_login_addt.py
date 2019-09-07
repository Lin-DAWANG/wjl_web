from selenium import webdriver
import unittest
from pages.login_page import LoginPage,login_url
from common.read_excel import ExcelUtil
import ddt
import os


'''
1：输入admin，输入123456，登录
2：输入admin，输入        登录
3：输入qqq，输入123456  ，登录
4：忘记密码
'''

# testdatas = [
#     {"user":"admin","pwd":"123456","expect":"admin"},
#     {"user":"admin","pwd":"","expect":""},
#     {"user":"admin123","pwd":"123456","expect":""}
#     ]
# os.path.realpath(__file__)获取当前脚本的真实路径  os.path.dirname 上一层路径
# pro_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
# filepath = os.pro_path.join(pro_path,"common","datas.xls")

filepath = "D:\PycharmProjects\web_auto\common\datas.xls"
data = ExcelUtil(filepath)
testdatas = data.dict_data()
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

    def login_case(self,user,pwd,expect): # 此为用例 不是方法
        self.login_step.input_user(user)
        self.login_step.input_pwd(pwd)
        self.login_step.click_submit()
        # self.login_step.login(user,pwd,) # 此为调用方法
        result = self.login_step.get_login_name()
        print("测试结果：%s"%result)
        self.assertTrue(result == expect)
    @ddt.data(*testdatas)
    def test_(self,data): # 执行三条用例
        '''输入账号admin，输入密码123456，登录,验证结果'''
        # data = testdatas[0]
        print("-------01测试数据：%s--------"%data)
        self.login_case(data["user"],data["pwd"],data["expect"])

    # def test_02(self):
    #     '''输入账号admin，不输入密码，登录,验证结果'''
    #     # data = testdatas[1]
    #     print("-------02测试数据：%s---------"%data)
    #     self.login_case(data["user"],data["pwd"],data["expect"])
    #
    # def test_03(self):
    #     '''输入账号admin，输入密码123456，记住密码登录,验证结果'''
    #     # data = testdatas[2]
    #     print("-------03测试数据：%s---------"%data)
    #     self.login_case(data["user"],data["pwd"],data["expect"])

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()


