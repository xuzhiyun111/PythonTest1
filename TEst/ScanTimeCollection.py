#!/usr/bin/python
#coding=utf-8

'''
@author: xuzhiyun
'''
#两个方向：1.动态获取日志的输出然后进行查看
#2.把日志输出到固定的文档然后对文档进行处理






# filesPlace = "D:/clean.log"
#   
# 
# try:
#     with open(filesPlace) as scanTimeCollection:
#         message = scanTimeCollection.read()
#         print(message)
#             
#         if 'onStart' in message:
#             time = message.split()[0]
#             print(time)     
#                            
# except FileNotFoundError:
#    print("No this files")
       

       


# filename = 'D:/clean.log'
# try:
#     with open(filename) as f_obj:
#         contents = f_obj.read()
#         print(conents)
#         
# except FileNotFoundError:
#         msg = "Sorry, the file " + filename + " does not exist."
#         print(msg)