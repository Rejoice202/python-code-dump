#!/usr/bin/python
# -*- coding: UTF-8 -*-

def nextNum(num):
	s = [x for x in str(num)]
	# print "s",s
	for i in range(len(s)-1,-1,-1):
		# print "i,s[i]",i,s[i]
		if s[i]>s[i-1]:
			switched = i-1
			# print "switched",switched
			break
	# print "s[switched]",s[switched]
	for i in range(len(s)-1,switched,-1):
		if s[i]>s[switched]:
			switch = i
			# print "switch",switch
			break
	# print "s[switch]",s[switch]
	s[switch], s[switched] = s[switched], s[switch]
	last = s[switched+1:]
	last.reverse()
	# print(s[:switched+1]+last)
	return ("".join(s[:switched+1]+last))
	
num = 12532
num = 56976
print(nextNum(num))
