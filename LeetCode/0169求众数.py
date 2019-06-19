#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0169求众数.py
# @Time    :   2019-05-15 21:43:06
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def majorityElement(nums):
	len_nums = len(nums)
	if not len_nums:
		return
	set_nums = set(nums)
	for num in set_nums:
		if nums.count(num) > len_nums/2:
			return num
	
	# print(nums_dict)

if __name__ == '__main__':
	nums = [2,2,1,1,1,2,2]
	result = majorityElement(nums)
	print(result)