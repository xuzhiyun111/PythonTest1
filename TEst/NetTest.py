#!/usr/bin/python
#coding=utf-8
import os
import time

class NetdataTest():

    def __init__(self,count):
        self.counter = count
        self.collectData = ['NetData']

    
    def startCollect(self):
        pid_cmd = 'adb shell ps | grep com.meizu.flyme.find'  
        pidNet_cmd = 'adb shell cat /proc/pid/net/dev' 
        pid = os.popen(pid_cmd)
        pidData = pid.readlines()[0].split(' ')[3] 
        print(pidData)
        pidNet_cmd = 'adb shell cat /proc/'+ pidData + '/net/dev' 
        pidNetData = os.popen(pidNet_cmd)
        for lines in pidNetData.readlines():
            if 'wlan0:' in lines:
                allNetData = int(lines.split()[1]) + int(lines.split()[9])
                print(allNetData)
                
    def runNetData(self):
        while self.counter > 0:
            self.startCollect()
            time.sleep(15)
            self.counter = self.counter - 1
        


    def saveData(self):
        file = 'collectNetDate.txt'
        with open(file,'w') as files:
            for row in self.collectData:
                files.write(row)

test = NetdataTest(5)
test.startCollect()

