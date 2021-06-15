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
        myurl = "http://safe.meizu.com/service/ads/vw?imei=866774030039369&sn=881QADRTC2MFC&aids=[1528789574986200]&op=1&sign=2aa738fd049e2bddb38f9e74aa1fa5d1"
        result = requests.get(myurl,None)
        print(i)    
   
for i in range(60):
    t = threading.Thread(target=run, args=(i,))   
    t.start()     