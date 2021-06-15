# -*- coding:utf-8 -*-
import os
import time
import configparser
import subprocess
from _ast import Str
from uiautomator import device as d


project_root = os.path.dirname(os.path.realpath(__file__))
file_path = os.path.join(project_root + '\config.ini')
print(file_path)

rf = configparser.ConfigParser()
rf.read(file_path)

class runMonkey():
    def __init__(self):
        
        self.check_time = rf.get("activity", "check_time")
        self.whileActivity = rf.get("activity", "whileActivity")
        self.counts = rf.get("activity", "counts")
        self.mainActivity = rf.get("activity", "mainActivity")
        self.logActivity = rf.get("activity","logActivity")
        
    def connectDevices(self):
        self.devicesCode = subprocess.check_output('adb devices').decode().split('\r\n')
        try:
            if self.devicesCode[1]  == '':
                return False
            else:
                return True
        except Exception:
            print('connecting devices is failed:')
            return False
        
    def loginApp(self):
        #print("控件1")
        d(resourceId = 'com.meizu.find.watch:id/username').set_text("18818654110")
        d(resourceId = 'com.meizu.find.watch:id/passwords').set_text("test123456789")
        d.click(1025, 1392)
        d(resourceId = 'com.meizu.find.watch:id/btn_login').click()
        #print("控件2")

        
    def get_now_activity(self):
        
        if False == self.connectDevices():
            print('no device connect!')
            return
        
        os.system("adb devices")
        content = os.popen('adb shell dumpsys activity | findstr "mResumedActivity"').read()
        contentString = ''.join(content)
        currentActivity = contentString.split()[3]
        
        excuteMain = 'adb shell am start -n' + self.logActivity
        
        if currentActivity not in self.whileActivity:
            print("当前Activity：" + contentString)
            print("重新登录账号进入主Activity")
            os.system(excuteMain)
            self.loginApp()            
            
        else:
            print("当前Activity：" + content)
            
    def check(self):
        for x in range(int(self.counts)):
            print("----当前正在执行第：" + str(x) + "次------")
            
            time.sleep(int(self.check_time))
            self.get_now_activity()
            
if __name__ == '__main__':
    run = runMonkey()
    run.check()
        
        
        