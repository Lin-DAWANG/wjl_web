from  selenium import webdriver
from pages.login_page import LoginPage
import time

class t_01():
    driver = webdriver.Firefox()
    a = LoginPage(driver)
    a.login()

    driver.get("http://127.0.0.1:81/zentao/bug-create-1-0-moduleID=0.html")
    # js不需要切换iframe
    time.sleep(3)
    body = "hello world"
    js = "document.getElementsByClassName('ke-edit-iframe')[0].contentWindow.document.body.innerHTML='%s'"%body
    driver.execute_script(js)

class t_02():
    driver = webdriver.Firefox()
    driver.get("https://www.12306.cn/index/")
    time.sleep(3)

    js1 = '''document.getElementById("train_date").removeAttribute("readonly");
             document.getElementById("train_date").value="2018-09-12"
    '''
    driver.execute_script(js1)

    driver.find_element_by_id("train_date").clear()
    driver.find_element_by_id("train_date").send_keys("280")

if __name__ == "__main__":
    t_02()