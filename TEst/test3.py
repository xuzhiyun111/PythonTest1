#!/usr/bin/python
#coding=utf-8
'''
@author: xuzhiyun
'''
import unittest
import os
from uiautomator import device as d

#判断元素是否存在的方法
def assert_exists(cm):
    
    if cm.exists:
        return True
    else:
        return False


class Test(unittest.TestCase):
    
    def testCase358(self):
#         cmd_ClearDate = "adb shell pm clear com.meizu.safe"
#         os.system(cmd_ClearDate)
        cmd_startAPP = "adb shell am start -W -n  com.meizu.safe/.SecurityMainActivity"
        os.system(cmd_startAPP)
        assert_exists(cm = d(text = '手机管家需要连接网络、获取定位、使用相机，以更新病毒库、提供流量校准与安全扫码功能'))
        assert_exists(cm = d(text = '退出'))
        assert_exists(cm = d(text = '确定'))
        message1 =  d(resourceId = 'com.meizu.safe:id/mc_pm_textView')
        self.assertTrue("手机管家需要连接网络、获取定位、使用相机，以更新病毒库、提供流量校准与安全扫码功能", message1)
                    
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()