#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0191位1的个数.py
# @Time    :   2019-05-16 18:44:43
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib

def hammingWeight(n):
	# return bin(n).count('1')
	count = 0
	while n:
		count += n&1
		n >>= 1
	return count


if __name__ == '__main__':
	n = 987
	print(hammingWeight(n))