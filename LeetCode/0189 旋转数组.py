#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0189 旋转数组.py
# @Time    :   2019-05-17 22:06:28
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def rotate(nums, k):
	# list_in = nums[-k:]
	# list_in.extend(nums)
	# nums = list_in[:-k]
	# print(nums)

	# list_in = nums[-k:]
	# nums[-k:].extend(nums)
	# # nums = nums[:-k]
	# print(nums)


	# for i in range(k):
	# 	nums.insert(0, nums.pop(-1))
	# 	print(nums)
	k = k%len(nums)
	nums[:] = nums[-k:]+nums[:-k]


if __name__ == '__main__':
	nums = [1,2,3,4,5,6,7] 
	k = 3
	rotate(nums, k)