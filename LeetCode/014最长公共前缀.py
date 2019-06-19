#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   014最长公共前缀.py
# @Time    :   2019-05-11 19:50:00
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib

def longestCommonPrefix(strs):
	if not strs: 
		return ""
	s1 = min(strs)
	s2 = max(strs)
	for i,x in enumerate(s1):
		if x != s2[i]:
			return s2[:i]
	return s1
	# print(k)
	# if k==0:
	# 	return ''
	# else:
	# 	return strs[0][:k-1]

if __name__ == '__main__':
	strs = ["flower","flow","flight"]
	result = longestCommonPrefix(strs)
	print(result)