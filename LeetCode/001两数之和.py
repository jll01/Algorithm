#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   001两数之和.py
@Time    :   2019/05/06 17:07:23
@Author  :   LJL
@Version :   1.0
@Contact :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None
'''
# here put the import lib


def twoSum(nums, target):
    len_nums = len(nums)
    index = []
    # for i in range(len_nums):
    #     for j in range(i+1, len_nums):
    #         if nums[i] + nums[j] == target:
    #             index.append((i,j))
    #             break
    # num_copy = nums[:]
    for i in range(len(nums)-1):
        result = target - nums[i]
        num_copy = nums[i+1:]
        if result in num_copy:
            index.append([i, num_copy.index(result)+i+1])            

    # return index
    hashmap = {}
    for index, num in enumerate(nums):
        another_num = target - num
        if another_num in hashmap:
            return [hashmap[another_num], index]
        hashmap[num] = index
    return None


if __name__ == '__main__':
    nums = [4, 4, 11, 0, 8, 9, 15, 3, 6, 5, 4, 1, 8]
    target = 8
    result = twoSum(nums, target)
    print(result)
