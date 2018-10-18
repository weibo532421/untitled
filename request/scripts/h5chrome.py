from selenium import webdriver
from time import sleep


class Test_mmmoney():

    def __init__(self):
        self.driver=webdriver.Chrome()

    def login(self,phone,password):
        driver =self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        base_url='https://site-wap.88mmmoney.com/index.htm'
        driver.get(base_url)
        driver.find_element_by_link_text("注册使用").click()
        driver.find_element_by_id("phone-num").clear()
        driver.find_element_by_id("phone-num").send_keys(phone)
        sleep(2)
        driver.find_element_by_id("login-password").clear()
        driver.find_element_by_id("login-password").send_keys(password)
        driver.find_element_by_id("loginOrReg").click()
        sleep(5)
    def loginout(self):
        driver=self.driver
        driver.find_element_by_xpath('//*[@id="allBody"]/div[1]/div/div/div/a[4]/i').click()
        driver.find_element_by_xpath('//*[@id="allBody"]/div[1]/div/section[1]/span').click()
        driver.find_element_by_id('logout').click()
        driver.find_element_by_xpath('//*[@id="layermbox0"]/div[2]/div/div/div[3]/span[2]').click()
        sleep(2)
        driver.quit()