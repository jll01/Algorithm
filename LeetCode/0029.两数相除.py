#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0029.两数相除.py
# @Time    :   2019-05-21 15:37:35
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def divide(dividend, divisor):
	byte_dividend = bin(dividend)
	byte_divisor = bin(divisor)
	print(byte_dividend/byte_divisor,bin(7//3))

if __name__ == '__main__':
	dividend = 7
	divisor = 3
	result = divide(dividend, divisor)
	print(result)