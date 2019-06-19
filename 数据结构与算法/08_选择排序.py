#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   08_选择排序.py    
@Time    :   2019/4/7 17:58:29
@Author  :   LJL
@Version :   1.0
@Email   :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


import random


def select_sort(alist):
    """选择排序 最坏情况O(n^2)"""
    len_list = len(alist)
    for i in range(len_list-1):
        for j in range(i+1, len_list):
            if alist[j] < alist[i]:
                alist[j], alist[i] = alist[i], alist[j]

    return alist


if __name__ == '__main__':
    list_test = [random.randint(0, 100) for _ in range(10)]
    print(list_test)
    b = select_sort(list_test)
    print(b)
    if b == sorted(list_test):
        print('验证成功')
