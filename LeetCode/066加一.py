#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   066加一.py
# @Time    :   2019-05-11 19:16:11
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def plusOne(digits):
	str_digits = 0
	list_digits = []
	for i in range(0,len(digits)):
		str_digits += digits[i] * 10**(len(digits)-i-1)

	str_digits = str(int(str_digits) + 1)
	for i in str_digits:
		list_digits.append(int(i))
	return list_digits

	
	# num = int(''.join(list(map(str, digits))))+1
	# return list(map(int, list(str(num))))



if __name__ == '__main__':
	digits = [9,9]
	result = plusOne(digits)
	print(result)