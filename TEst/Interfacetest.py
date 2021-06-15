#!/usr/bin/python
#coding=utf-8
'''
@author: xuzhiyun
'''
import unittest
import requests
import urllib.request 
import threading   
import time
from ddt import ddt,data,unpack

@ddt
class Test(unittest.TestCase):

#     #RequestMetodUser
#     @data(("7.0.1","5001041"),("",""),("haode","5001051"),("8.1.0-","5001041"))
#     @unpack
#     def testRequest(self,fmversion,safeversion):
#         myurl = "http://safe.meizu.com/service/cfg/news?imei=868455030020918&sn=892QAESNYSKP2&fmver="+fmversion+"&sfver="+safeversion +"&mdl=M8920&sign=5657215dfd16c65c1448a177a0e810c2"
#         result = requests.get(myurl,None)
#         self.assertEqual(200, result.status_code, "Pass")
# #         print(result.status_code)
  
    def testUrllibTest(self):
        response = urllib.request.urlopen('http://www.baidu.com/') #urllib.request ==urlib2
        print(response.getcode())

#     def testRequest1(self):
#         for i in range(100):
#             myurl = "http://safe.meizu.com/service/ads/vw?imei=866778030050474&sn=882QAESSYF3DC&aids=[1533046508122002]&op=1&sign=551095a693fb391e0a6f62c56122ae48"
#             result = requests.get(myurl,None)
            

if __name__ == "__main__":
    unittest.main()