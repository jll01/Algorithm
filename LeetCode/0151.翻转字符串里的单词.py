#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0151.翻转字符串里的单词.py
# @Time    :   2019-05-18 15:28:40
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def reverseWords(s):
	s = s.split()[::-1]
	print(s)
	# while '' in s:
	# 	s.remove('')
	return ' '.join(s)
	# return " ".join(s.strip().split()[::-1])


if __name__ == '__main__':
	s = "  hello world!  "
	print(reverseWords(s))