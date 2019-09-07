# coding:utf-8
from selenium import webdriver
from common.base import Base
import time

login_url = "http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html"

class LoginPage(Base):
    # 定位登录
    loc_user = ("id","account")
    loc_pwd = ("css selector","[name='password']")
    loc_submit = ("xpath",".//*[@id='submit']")
    loc_keep = ("id","keepLoginon")
    loc_forget_psw = ("link text","忘记密码")

    loc_get_username = ("css selector","#userMenu>a")

    loc_forget_page = ("xpath","//div[@class='panel-body']/p/a")

    def input_user(self,text=""):
        self.sendKeys(self.loc_user,text)

    def input_pwd(self,text=""):
        self.sendKeys(self.loc_pwd,text)

    def click_submit(self):
        self.click(self.loc_submit)

    def click_keep_login(self):
        self.click(self.loc_keep)

    def click_forget_psw(self):
        self.click(self.loc_forget_psw)


    # def login(self,user="admin",pwd="123456"):
    #     self.sendKeys(self.loc1,user)
    #     self.sendKeys(self.loc2,pwd)
    #     self.click(self.loc3)
    def get_login_name(self):
        user = self.get_text(self.loc_get_username)
        return user

    def get_login_result(self,user):
        result = self.is_text_in_element(self.loc_get_username,user)
        return result # true false

    def is_alert_exist(self):
        '''判断alert是否存在'''
        a = self.is_alert()
        if a:
            print(a.text)
            a.accept()
        else:
            pass

    def login(self,user="admin",pwd="123456",keep_login=False):
        '''登录流程'''
        self.driver.get(login_url)
        self.input_user(user)
        self.input_pwd(pwd)
        if keep_login: self.click_keep_login() # 默认不点击，传参为true时点击
        self.click_submit()


    def is_forgrt_page_exist(self):
        '''判断忘记密码页（刷新）'''
        r = self.is_text_in_element(self.loc_forget_page)
        return r



if __name__ == "__main__":
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)
    driver.get(login_url)
    login_page.input_user("admin")
    login_page.input_pwd("123456")
    login_page.click_keep_login()
    login_page.click_submit()


