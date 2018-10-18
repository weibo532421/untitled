from appium import webdriver
import os
import selenium
from time import sleep


class Test_app():


    def test(self,phone,password):

        descrip_caps={}
        descrip_caps['platformName']='Android'
        descrip_caps['platformVersion']='8.0.0'
        descrip_caps['deviceName']='Honor 8 Lite'
        descrip_caps['appActivity']='com.mmmoney.app.activity.MaSplashActivity'
        descrip_caps['appPackage']='com.mmmoney.app'
        descrip_caps['unicodeKeyboard']=True
        descrip_caps['resetKeyboard']=True
        driver=webdriver.Remote('http://localhost:4723/wd/hub',descrip_caps)


        driver.implicitly_wait(10)
        driver.find_element_by_id('com.mmmoney.app:id/guide_skip_1').click()
        driver.find_element_by_id('com.mmmoney.app:id/guide_go').click()
        sleep(3)
        driver.find_element_by_id('com.mmmoney.app:id/tv_fragment_new_index_register').click()
        # driver.find_element_by_id('com.mmmoney.app:id/et_activity_login_and_register_mobile').clear()
        driver.find_element_by_id('com.mmmoney.app:id/et_activity_login_and_register_mobile').send_keys(phone)
        driver.implicitly_wait(10)
        driver.find_element_by_id('com.mmmoney.app:id/et_activity_login_and_register_login_password').send_keys(password)
        driver.back()

        driver.find_element_by_id('com.mmmoney.app:id/btn_activity_login_and_register_login').click()
        sleep(3)
        driver.find_element_by_id('com.mmmoney.app:id/titlebar_right_text').click()
        sleep(3 )
        driver.find_element_by_xpath('//android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[4]').click()
        driver.find_element_by_id('com.mmmoney.app:id/iv_fragment_wallet_setting').click()
        driver.find_element_by_id('com.mmmoney.app:id/btn_activity_setting_logout').click()
        driver.find_element_by_id('com.mmmoney.app:id/btn_dialog_alert_option_confirm').click()
        sleep(2)
        driver.quit()


