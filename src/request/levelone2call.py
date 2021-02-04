#!/usr/bin/env python
#coding=utf-8
import json
import sys
import time, md5, string
import urllib2
import os
import requests 

if __name__ == '__main__':
	#请求点击拨号URL
    url = 'http://127.0.0.1:6081/appcall/v1/TwoPartiesCall'
	#appid
    #appid = "10000000130"
	#密码
    #secret = "DB2F8822DB7D4823A89A1FA0FDEA2610"
    appid = "A_992770E178AB4C339BF384FE16B473"
    secret = "8837420D846248E28E55F7780966C736"
	#sponsor：主叫C号码 ，display：来显号码 ，caller：主叫 ，callee ：被叫 
    body_dict = {"sepid":"eop.sc.chinamobile.com", "sponsor": "0529002624","caller": "8613900090001",
                 "callee": "8613900090002", "APPID": appid, "APIID" : "50015"}
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



