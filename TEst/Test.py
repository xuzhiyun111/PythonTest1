# -*- coding:utf-8 -*-
import os
import time

class TrafficTest():
    def __init__(self,times,pid,field_name):
        self.times=times
        self.pid=pid
        self.field_name=field_name
        self.lastbytes=0  
    #获取当前时间
    def getCurrentTime(self):
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        return currentTime  
    #单次统计流量并计算差值
    def test(self):
        self.content=""
        thisbytes=0
        Added_traffic=0
        cmd='adb shell cat /proc/'+str(self.pid)+'/net/dev'
        self.content_1=os.popen(cmd)
        curr_time=self.getCurrentTime()
       
        filename=r'D:\traffic.txt'
        with open(filename,'a') as file_object:
            for line in self.content_1.readlines():
                file_object.write(line)
                if str(self.field_name) in line:
                    rxBytes=line.split()[1]
                    txBytes=line.split()[9]
                    thisbytes=int(rxBytes)+int(txBytes)
                
            if self.lastbytes!=0:
                Added_traffic=thisbytes-self.lastbytes
            file_object.write("currentTime: "+str(curr_time)+"\n")
            file_object.write("thisbytes: "+str(thisbytes)+"\n")
            file_object.write("self.lastbytes: "+str(self.lastbytes)+"\n")
         
            self.lastbytes=thisbytes  
                   
            file_object.write("Added_traffic: "+str(Added_traffic)+"\n")
            
        
    #执行测试
    def runTest(self):
        while self.times>0:
            self.test()
            os.popen("adb shell pm clear com.meizu.safe")
            time.sleep(5)
            os.popen("adb shell am start com.meizu.safe/.SecurityMainActivity")
            time.sleep(10)
            self.times=self.times-1
            
        print("test run success")
traffictest=TrafficTest(11,2688,"wlan0")
traffictest.runTest()
        