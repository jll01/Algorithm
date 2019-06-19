#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   07_冒泡排序.py    
@Time    :   2019/4/7 17:20:32
@Author  :   LJL
@Version :   1.0
@Email   :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


import random

def bubble_sort(alist):
    """冒泡排序 最坏情况O(n^2)"""
    for j in range(len(alist)-1):
        for i in range(len(alist)-1-j):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

    return alist


if __name__ == '__main__':
    list_test = [random.randint(0, 100) for _ in range(10)]
    print(list_test)
    b = bubble_sort(list_test)
    print(b)
