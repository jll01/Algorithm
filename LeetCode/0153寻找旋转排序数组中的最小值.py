#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0153寻找旋转排序数组中的最小值.py
# @Time    :   2019-05-18 15:45:22
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def findMin(nums):
	# if len(nums) != len(set(nums)):
	# 	return
	# if len(nums) == 1:
	# 	return nums
	# for i in range(len(nums)-1):
	# 	if nums[i] > nums[i+1]:
	# 		return nums[i+1]

	left,right = 0,len(nums)-1
	while left<right:
		mid = (left+right)//2
		if nums[mid]<nums[right]:
			right = mid
		else:
			left = mid+1
	return nums[left]




if __name__ == '__main__':
	nums = [4,5,6,7,8,0,1,2,3,4]
	print(findMin(nums))