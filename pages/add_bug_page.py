# coding:utf-8
from selenium import webdriver
from common.base import Base
import time
from pykeyboard import PyKeyboard

class AddBugPage(Base):
    # 定位登录
    loc1 = ("id","account")
    loc2 = ("css selector","[name='password']")
    loc3 = ("xpath",".//*[@id='submit']")

    # 添加bug
    loc_test = ("link text","测试")
    loc_bug = ("link text","Bug")
    loc_addbug = ("xpath",".//*[@id='createActionMenu']/a")
    loc_trunk = ("xpath",".//*[@id='openedBuild_chosen']/ul")
    loc_truck_add = ("xpath",".//*[@id='openedBuild_chosen']/div/ul/li")
    loc_input_title = ("id","title")
    #需要先切换
    loc_input_body = ("class name","article-content")
    loc_submit = ("css selector","#submit")

    # 验证
    loc_new = ("xpath",".//*[@id='bugList']/tbody/tr[1]/td[4]/a")

    up = ("xpath",".//*[@id='dataform']/table/tbody/tr[6]/td/div[2]/div[1]/span[18]/span")
    sub = ("css selector",".ke-inline-block.ke-upload-button")

    # 直接继承Base类不需要实例化
    # def __init__(self,driver):
    #     self.driver = driver
    #     self.zentao = Base(driver)

    def login(self,user="admin",pwd="123456"):
        self.sendKeys(self.loc1,user)
        self.sendKeys(self.loc2,pwd)
        self.click(self.loc3)

    def add_bug(self,title="测试bug"):
        self.click(self.loc_test)
        self.click(self.loc_bug)
        self.click(self.loc_addbug)
        self.click(self.loc_trunk)
        self.click(self.loc_truck_add)

        self.sendKeys(self.loc_input_title,title)

        frame = self.findElement(("class name","ke-edit-iframe"))
        self.driver.switch_to.frame(frame)
        # 富文本不能用clear
        context = '''
        [步骤]
        [期望结果]
        '''


        self.sendKeys(self.loc_input_body,context)
        self.driver.switch_to.default_content()
        self.click(self.loc_submit)

    def is_add_bug_success(self,_text):
        return self.is_text_in_element(self.loc_new,_text)


if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:81/zentao/user-login.html")
    bug = AddBugPage(driver)

    bug.login()

    timestr = time.strftime("%Y_%m_%d_%H_%M_%S")
    title = "提交测试bug"+timestr
    bug.add_bug(title)

    result = bug.is_add_bug_success(title)
    print(result)



