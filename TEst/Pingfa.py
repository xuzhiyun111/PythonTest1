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
    for i in range(10):
        myurl = "http://safe.meizu.com/service/ads/vw?imei=866777030058255&sn=891QBDS72229G&aids=[1576042880122009]&op=1&sign=30696a0a85096fdd6a5e10dac3ea603c"
        result = requests.get(myurl,None)
        print(i)    
   
for i in range(10):
    t = threading.Thread(target=run, args=(i,))   
    t.start()     