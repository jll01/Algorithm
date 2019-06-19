#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0171Excel表列序号.py
# @Time    :   2019-05-16 18:16:32
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def titleToNumber(s):
	if s.strip(' ') == '':
		return 
	res = 0
	# s = s[::-1]
	for i in range(len(s)):
		res = res*26 + (ord(s[i]) - 64)
	return res


if __name__ == '__main__':
	s = "ZY"
	result = titleToNumber(s)
	print(result)