#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   002两数相加.py
# @Time    :   2019-05-11 21:15:28
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def addTwoNumbers(l1, l2):
	int1 = int(''.join(list(map(str, l1[::-1]))))
	int2 = int(''.join(list(map(str, l2[::-1]))))

	str_num = str(int1 + int2)

	return list(map(int, str_num))[::-1]


if __name__ == '__main__':
	l1 = [2,4,3]
	l2 = [5,6,4]
	result = addTwoNumbers(l1, l2)
	print(result)