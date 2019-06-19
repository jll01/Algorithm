#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   0198打家劫舍.py
# @Time    :   2019-05-16 21:32:46
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def rob(nums):        
	if nums==[]:
	    return 0
	len_nums=len(nums)
	if len_nums < 3:
	    return max(nums)
	else:
	    dp = [0]*(len_nums+1)
	    dp[0] = 0
	    dp[1] = nums[0]
	    dp[2] = nums[1]
	    for i in range(3,len_nums+1):
	        dp[i] = max(dp[i-2],dp[i-3]) + nums[i-1] 
	        print(dp[i-2],dp[i-3],nums[i-1])
	        print(dp) 	        
	    return max(dp[-2],dp[-1]) 


if __name__ == '__main__':
	nums = [2,1,1,2]
	print(rob(nums))