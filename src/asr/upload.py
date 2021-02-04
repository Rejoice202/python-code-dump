#!/usr/bin/python
#coding:utf-8

import os, sys
import base64
import httplib, urllib

import json
import sys
import time, md5, string
import urllib2
import os
import requests 

# fileName = "01_-_That_Time_I_Got_Reincarnated_as_a_Slime.mp3"
# fileName = "KOE.mp3"
fileName = "_20170929100047.jpg"



def getFile(fileName):
	f = open(fileName, mode='rb')
	print(type(f))
	data = base64.b64encode(f.read())
	print(type(data))
	print(len(data))
	return len(data),data
	
	
	
if __name__ == '__main__':
	url = 'http://127.0.0.1:9080/voiceserver/v1/tencent_asr_upload'
	# url = 'http://123.56.15.3:9080/voiceserver/v1/tencent_asr_upload'
	
	FileSize,FileData = getFile(fileName)

	body_dict = {"FileName": fileName, "FileData":FileData, "FileSize":FileSize}
	# body_dict = {"FileName": fileName, "FileSize":FileSize}
	body = json.dumps(body_dict)
	# print body
	
	header = {"Content-type": "application/json"}
	print("ready to post")
	result = requests.post(url,data=body,headers=header)
	print result.text
	print result