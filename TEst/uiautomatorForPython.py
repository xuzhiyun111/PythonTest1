#!/usr/bin/python
#coding=utf-8
from uiautomator import device as d
import os,unittest
from ddt import data,ddt,unpack
from appium import webdriver

#判断元素是否存在的方法
def assert_exists(cm):
    
    if cm.exists:
        return False
    else:
        return True
@ddt
class Test(unittest.TestCase):
 
#     #初始函数   
#     def setUp(self):
#         cmd_startAPP = "adb shell am start -W -n  com.meizu.flyme.find/.ui.LoginActivity"
#         os.system(cmd_startAPP)
#     #结束函数  
#     def tearDown(self):
#         cmd_closeAPP='adb shell am force-stop com.meizu.flyme.find'
#         os.system(cmd_closeAPP)
#     
#     @data(("faty111@flyme.cn","faty1111"),("faty111","faty1111"),("",""),("faty","faty111"),) 
#     @unpack 
#     def testlogin(self,UserName,Password):
#         d(resourceId = 'com.meizu.flyme.find:id/edtTxt_userName').set_text("")
#         d(resourceId = 'com.meizu.flyme.find:id/edtTxt_userName').set_text(UserName)
#         d(resourceId = 'com.meizu.flyme.find:id/edtTxt_password').set_text(Password)
#         d(resourceId = 'com.meizu.flyme.find:id/btn_login').click()
#         assert_Login = assert_exists(cm = d(resourceId = 'com.meizu.flyme.find:id/btn_login'))
#         self.assertTrue(assert_Login)

   #appium TestforNative configure
    def setUp(self):
        self.desired_caps = {}
        self.desired_caps['platformName'] = 'Android'
        self.desired_caps['platformVersion'] = '8.1.0'
        self.desired_caps['deviceName'] = '872QADT4XYFCJ'
        self.desired_caps['appPackage'] = 'com.meizu.flyme.find'
        self.desired_caps['appActivity'] = '.ui.LoginActivity'
        self.desired_caps["unicodeKeyboard"] = True
        self.desired_caps["resetKeyboard"] = True
        self.driver = webdriver.Remote('http://localhost:4724/wd/hub',self.desired_caps)
        
    def tearDown(self):
        self.driver.quit()
        
    def testLogin(self):
        login_button = self.driver.find_elements_by_id("btn_login")
        login_button.click()
        
        
#主函数       
if __name__=='__main__':
    unittest.main();
        
    
#     d(text="手机瘦身").click()
#     d.wait(d(text="建议清理").exists,1)
#     deviceInfo = d.info
#     print(deviceInfo)
 

               

