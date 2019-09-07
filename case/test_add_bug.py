# coding:utf-8
from selenium import webdriver
from pages.add_bug_page import AddBugPage
from pages.login_page import LoginPage
import unittest
import time

class Test_Add_Bug(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.get("http://127.0.0.1/zentao/user-login-L3plbnRhby8=.html")
        cls.bug = AddBugPage(cls.driver)
        cls.a = LoginPage(cls.driver)
        cls.a.login()

    def test_add_bug(self):
        timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
        title = "提交测试bug"+timestr
        self.bug.add_bug(title)

        result = self.bug.is_add_bug_success(title)
        print(result)
        self.assertTrue(result)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

if __name__ == "__main__":
    unittest.main()

