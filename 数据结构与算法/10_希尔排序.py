#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   10_希尔排序.py
@Time    :   2019/4/7 22:01:52
@Author  :   LJL
@Version :   1.0
@Email   :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


import random


def shell_sort(alist):
    """希尔排序"""
    n = len(alist)
    gap = n // 2
    while gap >= 1:
        for i in range(gap, n):
            for j in range(i, 0, -gap):
                if alist[j] < alist[j-gap]:
                    alist[j], alist[j-gap] = alist[j-gap], alist[j]
                else:
                    break
        gap //= 2

    return alist


if __name__ == '__main__':
    list_test = [random.randint(0, 100) for i in range(random.randint(8, 15))]
    print('原来的列表:\t{}'.format(list_test))
    print('sorted排序:\t{}'.format(sorted(list_test)))
    insert_list = shell_sort(list_test)
    print('自定义排序:\t{}'.format(list_test))