#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0172 阶乘后的零.py
# @Time    :   2019-05-19 17:55:31
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def trailingZeroes(n):
	# sum_n = 1
	# while n:
	# 	sum_n *= n
	# 	n -= 1
	# count = 0
	# sum_n = str(sum_n)
	# len_n = len(sum_n)
	# for i in range(len_n):	
	# 	if sum_n[-1-i] == '0':
	# 		count += 1	
	# 	else:
	# 		break
	# return count


	if n < 5:
		return 0
	return n // 5 + trailingZeroes(n // 5)


if __name__ == '__main__':
	n = 10
	print(trailingZeroes(n))