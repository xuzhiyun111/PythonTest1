#!/usr/bin/python
#_*_coding:utf-8_*_
import unittest
from appium import webdriver
from time import sleep
import os
from HTMLTestRunner import *


class Test(unittest.TestCase):

    def __init__(self):
        
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '11'
        self.desired_caps['deviceName'] = '191QAEXTDYMD3'
        self.desired_caps['appPackage'] = 'com.meizu.flyme.find'
        self.desired_caps['appActivity'] = '.ui.LoginActivity'
        self.desired_caps["unicodeKeyboard"] = True
        self.desired_caps["resetKeyboard"] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',self.desired_caps)
        

    def tearDown(self):
        self.driver.quit()       


    def testLogin(self):
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
        sleep(5)
         
        el12 = self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.TextView[1]")
        self.assertEqual("m2172",el12)
        #print("hello selenium")
        

if __name__ == "__main__":

    run = Test()
    #import sys;sys.argv = ['', 'Test.testName']
    report = "./result.html"
    with(open(report, 'wb')) as fp:
        runner = HTMLTestRunner(
            stream=fp,
            title=u'Test',
            description=u'aaaaaaa'
        )
    runner.run(Test())
    report.close()