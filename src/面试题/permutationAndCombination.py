#!/usr/bin/python
# -*- coding: UTF-8 -*-

def permutationAndCombination(string):
	s = list(string)
	def dfs(x):
		if x == len(s)-1:
			print ''.join(s)
			return
		used = set()
		for i in range(x, len(s)):
			# print "x,i,used,s[x]",x,i,used,s[x]
			if s[i] in used:
				continue
			used.add(s[i])
			s[i], s[x] = s[x], s[i]
			dfs(x + 1)
			s[i], s[x] = s[x], s[i]
	dfs(0)

string = "abb"
permutationAndCombination(string)
