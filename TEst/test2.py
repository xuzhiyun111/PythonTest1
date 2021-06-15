#!/usr/bin/python
#coding=utf-8
from uiautomator import device as d
import os,unittest
from cgitb import text
from time import sleep

#判断元素是否存在的方法
def assert_exists(cm):
    
    if cm.exists:
        return True
    else:
        return False
    
class Test(unittest.TestCase):
 
    #初始函数   
    def setUp(self):
        d.press("home")
         
#     #结束函数  
    def tearDown(self):
        d.press("home")
      
    def testBigfile(self):
        cmd_fillFile = "adb push C:\\Users\\xuzhiyun\\Desktop\\bigfile.rar sdcard/"
        os.system(cmd_fillFile)
        cmd_startAPP = "adb shell am start -W -n  com.meizu.filemanager/com.meizu.flyme.filemanager.activity.HomeActivity"
        os.system(cmd_startAPP)
        d(resourceId = 'com.meizu.filemanager:id/r2_c1_tv').click()
        iscontinue = True
        while(iscontinue):
            sleep(3)
            d.long_click(586,571)
            d(text = '全选').click()
            d(text = '更多').click()
            d(text = '复制').click()
            d(text = '复制到这里').click()
            sleep(10)
            while(assert_exists(cm = d(text = '隐藏窗口'))):
                sleep(10)
            
            sleep(2)
            iscontinue = not assert_exists(cm = d(text = '存储空间不足')) 
            d.press("back")

    #测出来两个bug，一个是压缩到最后一个时勾选状态异常，一个是压缩最后一个返回可压缩不会显示空空如也           
    def testPicture1(self):
        cmd_startAPP = "adb shell am start -W -n com.meizu.safe/.SecurityMainActivity"
        os.system(cmd_startAPP)
        d(text = '手机瘦身').click()
        while(assert_exists(cm = d(text = '建议清理'))):
            sleep(10)
        d(scrollable=True).scroll(steps=5)
        d(text = '图片').click()
        d(text = '图片压缩').click()
        sleep(10)
        iscontinue = True
        while(iscontinue):
            iscontinue = not assert_exists(cm = d(text = '空空如也')) 
            print(iscontinue)
            if(iscontinue):
                d.click(367,505)
                d.click(358,856)
                sleep(2)
                #d(text = '确定').click()
                d.click(796,2507)
                d(text = '压缩').click()
                d(text = '可压缩').click()
            
                  

        d.press("home")  
        
    def testPicture2(self):
        cmd_startAPP = "adb shell am start -W -n com.meizu.safe/.SecurityMainActivity"
        os.system(cmd_startAPP)
        d(text = '手机瘦身').click()
        while(assert_exists(cm = d(text = '建议清理'))):
            sleep(10)
        for value in range(1,51):
            d(text = '图片').click()
            print(value)
            d(text = '图片压缩').click()
            sleep(5)
            d.click(57,169)
            sleep(5)
            d.click(57,169)
    
    def testSmartCard1(self):     
        
        for i in range(1,100):
            cmd_startAPP = "adb shell am start -W -n com.meizu.safe/.SecurityMainActivity"
            os.system(cmd_startAPP)
            d.press("back") 
        
    def testjusttest(self):     
        
        cmd_startAPP = "adb shell am start -W -n com.meizu.safe/.SecurityMainActivity"
        os.system(cmd_startAPP)
        d(text = '手机瘦身').click()
        while(assert_exists(cm = d(text = '共计可瘦身:'))):
            sleep(5)
        d(scrollable=True).scroll(steps=2)
        d(text = '图片').click()
        d(text = '屏幕截图').click()
        for value in range(1,100):
            sleep(2)
            d.click(333,1063)
            d.click(884,2460)
            d(text = '清理').click()
   
#主函数       
if __name__=='__main__':
    unittest.main();
        