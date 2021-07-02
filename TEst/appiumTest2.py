#!/usr/bin/python
#_*_coding:utf-8_*_
import unittest
from appium import webdriver
from time import sleep
import os



class Test():

    def __init__(self):

#         desired_caps ={'platformName':'Android','platformVersion':'8.1.0',

#                        'deviceName':'882qaesnrhlpg','appPackage':'com.meizu.flyme.find',

#                        'appActivity':'.ui.LoginActivity','unicodeKeyboard':'True','resetKeyBoard':'True',}

#         headers = {'Connection': 'close',}
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '11'
        self.desired_caps['deviceName'] = '181QGEXN222BW'
        self.desired_caps['appPackage'] = 'com.meizu.flyme.find'
        self.desired_caps['appActivity'] = '.ui.LoginActivity'
        self.desired_caps["unicodeKeyboard"] = True
        self.desired_caps["resetKeyboard"] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.desired_caps)
        

    def tearDown(self):
        self.driver.quit()       

    def testMonkey(self):
#自己写的        
#         permission_agree = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v7.widget.LinearLayoutCompat/android.widget.LinearLayout[2]/android.widget.Button[2]")
#         permission_agree.click()
#         sleep(1)
#         phone_allow = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")
#         phone_allow.click()
#         sleep(1)
#         location_allow = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")
#         location_allow.click()
#         sleep(1)
#         storge_alow = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.Button[1]")
#         storge_alow.click()
#         sleep(5)
#         login_name = self.driver.find_element_by_id("edtTxt_userName")
#         login_name.send_keys("faty111")
#         login_password = self.driver.find_element_by_id("edtTxt_password")
#         login_password.send_keys("faty1111")
#         login_in_button = self.driver.find_element_by_id("btn_login")
#         login_in_button.click()
#         sleep(10)

#appium自动录制的
        el1 = self.driver.find_element_by_id("android:id/button1")
        el1.click()
        sleep(2)
        el2 = self.driver.find_element_by_id("android:id/button1")
        el2.click()
        sleep(2)
        el3 = self.driver.find_element_by_id("android:id/button1")
        el3.click()
        sleep(2)
        el4 = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_one_time_button")
        el4.click()
        sleep(2)
        el5 = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_button")
        el5.click()
        sleep(2)
        el6 = self.driver.find_element_by_id("com.android.permissioncontroller:id/permission_allow_always_button")
        el6.click()
        sleep(2)
        el7 = self.driver.find_element_by_id("android:id/button2")
        el7.click()
        sleep(2)
        el8 = self.driver.find_element_by_id("com.meizu.flyme.find:id/e7")
        el8.send_keys("faty111")
        sleep(2)
        el9 = self.driver.find_element_by_id("com.meizu.flyme.find:id/e8")
        el9.send_keys("faty1111")
        sleep(2)
        el10 = self.driver.find_element_by_id("com.meizu.flyme.find:id/ea")
        el10.click()
        sleep(2)
        el11 = self.driver.find_element_by_id("android:id/button1")
        el11.click()
        sleep(3)
        #print("hello selenium")
        monkeyCommand = "adb shell monkey -p com.meizu.flyme.find --pct-touch 50 --pct-motion 15 --pct-anyevent 5 --pct-majornav 12 --pct-trackball 1 --pct-nav 0 --pct-syskeys 15 --pct-appswitch 2 --throttle 500  -v-v-v 1200000000"
        os.system(monkeyCommand)
        print("here")
        

if __name__ == "__main__":

    #import sys;sys.argv = ['', 'Test.testName']
    run = Test()
    run.testMonkey()