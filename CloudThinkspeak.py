# /usr/bin/python2
# Program to write data to thinkspeak server

import time
import httplib
import urllib
key="XXXXXXXXXXXXXXXXXXX" #api key
for i in range(10):
     a=input("enter the num")
     b=input("enter the num")
     params=urllib.urlencode({'field1':a,'field2':b,'key':key})
 
     headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
     conn = httplib.HTTPConnection("api.thingspeak.com:80")
     try:
          conn.request("POST", "/update", params, headers)
          response = conn.getresponse()
          #print( 'sending.....')
          #print( response.status, response.reason)
          data = response.read()
          conn.close()
          print("sucess")
     except:
          print( "connection failed")
