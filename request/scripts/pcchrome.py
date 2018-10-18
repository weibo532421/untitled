from selenium import webdriver
from time import sleep

class Pc_mmmoney():

    def __init__(self):
        self.driver=webdriver.Chrome()

    def login_in(self,phone,password):
        driver=self.driver
        driver.implicitly_wait(10)
        driver.maximize_window()
        base_url='https://mmmoney.mmzb.com/init.shtml'
        driver.get(base_url)
        driver.find_element_by_id('loginTop').click()
        driver.find_element_by_id('login_phone').clear()
        driver.find_element_by_id('login_phone').send_keys(phone)
        driver.find_element_by_id('login_pwd').clear()
        driver.find_element_by_id('login_pwd').send_keys(password)
        driver.find_element_by_id('loginBt').click()

    def login_out(self):
        driver=self.driver
        driver.find_element_by_link_text("安全退出").click()
        driver.quit()

