﻿#!/usr/bin/env python
#coding=utf-8
import json
import sys
import time, md5, string
import urllib2
import os
import requests 

if __name__ == '__main__':
	#请求点击拨号URL
    url = "http://127.0.0.1:6081/callnotification/v3/callcontrol/" + sys.argv[1]
	#appid
    appid = "A_04A2F0CC73944FAC889407752A301F"
	#密码
    secret = "DB2F8822DB7D4823A89A1FA0FDEA2610"
	#sponsor：主叫C号码 ，display：来显号码 ，caller：主叫 ，callee ：被叫 
    body_dict = {"sepid":"scep.cmcc.com","APIID ":"00003","operation":"EndCall"}
    body = json.dumps(body_dict)

    timetmp=time.time()
    timetmp=int(timetmp) 

    
    src=str(timetmp)+secret
    m1 = md5.new()
    m1.update(src)

    sign = m1.hexdigest()[-16:]
    print sign
    auth = "EOPAUTH appid=\'" + appid + "\',timestamp=\'" + str(timetmp) + "\',signature=\'" + sign + "\'"
    print auth
    header = {"Content-type": "application/json", "Authorization": auth}

    res = requests.post(url,data=body,headers=header)
    print res.text

    #req = urllib2.Request(url=url, data=body, headers=header)
    #res = urllib2.urlopen(req)
    #res = res.read()
    #print ("Request headers:", headers)
    #print ("Request body:", body)
    #print ("Response:", res)



