#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   12_归并排序.py    
@Time    :   2019/4/8 15:21:11
@Author  :   LJL
@Version :   1.0
@Email   :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


import random


def merge_sort(alist):
    """归并排序"""
    n = len(alist)
    if n <= 1:
        return alist
    mid = n // 2

    left_li = merge_sort(alist[:mid])
    right_li = merge_sort(alist[mid:])
    left_pointer, right_pointer = 0, 0
    result = []

    while left_pointer < len(left_li) and right_pointer < len(right_li):
        if left_li[left_pointer] < right_li[right_pointer]:
            result.append(left_li[left_pointer])
            left_pointer += 1
        else:
            result.append(right_li[right_pointer])
            right_pointer += 1

    result += left_li[left_pointer:]
    result += right_li[right_pointer:]

    return result


if __name__ == '__main__':
    list_test = [random.randint(0, 100) for i in range(random.randint(8, 15))]
    print('原来的列表:\t{}'.format(list_test))
    print('sorted排序:\t{}'.format(sorted(list_test)))
    res = merge_sort(list_test)
    print('自定义排序:\t{}'.format(res))




