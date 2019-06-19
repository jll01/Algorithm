#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0165.比较版本号.py
# @Time    :   2019-05-19 16:42:08
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def compareVersion(version1, version2):

	# v1_list = list(map(int, version1.split('.')))
	# v2_list = list(map(int, version2.split('.')))
	v1_list = [int(i) for i in version1.split('.')]
	v2_list = [int(i) for i in version2.split('.')]

	while v1_list and v2_list:
		v1_first, v2_first = v1_list.pop(0), v2_list.pop(0)
		if v1_first < v2_first:
			return -1
		elif v1_first > v2_first:
			return 1
	if v1_list and any(v1_list):
		return 1
	elif v2_list and any(v2_list):
		return -1
	return 0


if __name__ == '__main__':
	version1 = "1.0"
	version2 = "1"
	print(compareVersion(version1, version2))

