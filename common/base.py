from selenium import  webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select

class Base():
    def __init__(self,driver:webdriver.Firefox):
        self.driver = driver
        self.timeout = 10
        self.t = 0.5

    def findEle_01(self,locator):
        '''定位到元素返回元素对象，没定位到返回timeout异常'''
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元祖类型：loc=（'id','value'）")
        else:
            # print("正在定位元素信息：定位方式->%s,value值%s"%(locator[0],locator[1]))
            ele = WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))#传函数的对象 不加（driver）
            return ele
    def findElement(self,locator):
        # ele = WebDriverWait(driver, timeout, t).until(lambda x: x.find_element_by_id("kw"))
        # if not isinstance(locator,tuple):
        #     print("locator参数类型错误，必须传元祖类型：loc=（'id','value'）")
        # else:
        #     # print("正在定位元素信息：定位方式->%s,value值%s"%(locator[0],locator[1]))
        #     ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        #     return ele
        ele = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        return ele
    def findElements(self,locator):
        if not isinstance(locator,tuple):
            print("locator参数类型错误，必须传元祖类型：loc=（'id','value'）")
        else:
            try:
                # print("正在定位元素信息：定位方式->%s,value值%s"%(locator[0],locator[1]))
                eles = WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
                return eles
            except:
                return []

    def sendKeys(self,locator,text):
        ele = self.findElement(locator)
        ele.send_keys(text)

    def click(self,locator):
        ele = self.findElement(locator)
        ele.click()

    def clear(self,locator):
        ele = self.findElement(locator)
        ele.clear()

    def isSelected(self,locator):
        ele = self.findElement(locator)
        r = ele.is_selected()
        return r

    def isElemetExist(self,locator):
        try:
            ele = self.findElements(locator)
            return True
        except:
            return False
    def isElemetsExist(self,locator):
        eles = self.findElements(locator)
        n = len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            print("定位元素的个数：%"%n)
            return True

    def is_title(self,_title):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self,_title):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self,locator,_text):
        try:
            result = WebDriverWait(self.driver, self.timeout, self.t).until(EC.text_to_be_present_in_element(locator,_text))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result = WebDriverWait(self.driver,3, self.t).until(EC.alert_is_present)
            return result
        except:
            return False

    def get_title(self):
        return self.driver.title


    def get_text(self,locator):
        try:
            t = self.findElement(locator).text
            return t
        except:
            print("获取text失败，返回空")
            return ""

    def get_attributr(self,locator,name):
        try:
            element = self.findElement(locator)
            return element.get_attributr(name)
        except:
            print("获取attribute失败，返回空")
            return ""

    def move_to_element(self,locator):
        '''鼠标悬停操作'''
        ele = self.findElement(locator)
        ActionChains(driver).move_to_element(ele).perform()

    # select二次封装方法
    def select_by_index(self,locator,index=0):
        ele = self.findElement(locator)
        Select(ele).select_by_index(index)

    def select_by_value(self,locator,value):
        ele = self.findElement(locator)
        Select(ele).select_by_value(value)

    def select_by_text(self,locator,text):
        ele = self.findElement(locator)
        Select(ele).select_by_visible_text(text)

    #js操作浏览器滚动条
    def js_focus_element(self,locator):
        '''聚焦元素'''
        target = self.findElement(locator)
        self.driver.execute_script("argument[0].scrollIntoView()",target)

    def js_scroll_end(self,x=0): # x横向滚动
        '''滚动到底部'''
        js_heig = "window.scrollTo(%s,document. body.scrollHeight)"%x # 计算页面高度
        self.driver.execute_script(js_heig)

    def js_scroll_top(self):
        '''滚动到底部'''
        js_heig = "window.scrollTo(0,0)"
        self.driver.execute_script(js_heig)

if __name__ == "__main__":
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1:81/zentao/user-login-L3plbnRhby8=.html")
    zentao = Base(driver)

    # loc1 = (By.ID,"account")
    # loc2 = (By.NAME,"password")
    # loc3 = (By.ID,"submit")
    loc1 = ("id","account")
    loc2 = ("css selector","[name='password']")
    loc3 = ("xpath","//*[@id='submit']")
    loc4 = ("class name","xxx")
    zentao.sendKeys(loc1,"admin")
    zentao.sendKeys(loc2,"123456")
    zentao.click(loc3)
    zentao.get_title()
    driver.delete_all_cookies()

