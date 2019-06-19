#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0125验证回文串.py
# @Time    :   2019-05-15 20:10:31
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def isPalindrome(s):
	# if len(s.strip()) == 0:
	# 	return True
	# str_s = ''
	# for i in s:
	# 	if i.isalnum():
	# 		str_s += i
	str_s = ''.join(filter(str.isalnum, s)).lower()
	return str_s[::-1] == str_s



if __name__ == '__main__':
	# s = "A man, a plan, a canal: Panama"
	s = ' '
	result = isPalindrome(s)
	print(result)