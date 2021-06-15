# -*- coding:utf-8 -*-
'''
Created on 2019年9月9日

@author: xuzhiyun
'''

import threading    
import time
import requests
 
# def run(num):
#     print('Hi, I am thread %s..lalala' % num)
#     time.sleep(1)
#    
# for i in range(20):
#     t = threading.Thread(target=run, args=(i,))   
#     t.start()  
    
def run(num):
    for i in range(100):
        myurl = "http://safe.meizu.com/service/smartdevice/pkguuidlist?imei=866778030010031&sn=882QADSF5KD8E&sign=F510BA5681DA3DEA6CB71C32D3D12609"
        result = requests.get(myurl,None)
        if result.status_code != 200 :
            print("youwenti")    
   
for i in range(60):
    t = threading.Thread(target=run, args=(i,))   
    t.start()     
