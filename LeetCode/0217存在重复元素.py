#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0217存在重复元素.py
# @Time    :   2019-05-16 09:37:39
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def containsDuplicate(nums):
	set_nums = set(nums)
	if len(set_nums) == len(nums):
		return False
	return True


if __name__ == '__main__':
	nums = [7,3,2,1,2]
	result = containsDuplicate(nums)
	print(result)