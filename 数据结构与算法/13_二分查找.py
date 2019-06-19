#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   13_二分查找.py    
@Time    :   2019/4/8 17:02:48
@Author  :   LJL
@Version :   1.0
@Email   :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


import random


def binary_search(alist, item):
    """二分查找  递归"""
    n = len(alist)
    if n > 0:
        mid = n // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            return binary_search(alist[:mid], item)
        else:
            return binary_search(alist[mid+1:], item)
    return False


def binary_search_2(alist, item):
    """二分查找  非递归"""
    n = len(alist)
    first = 0
    last = n-1
    while first <= last:
        mid = (first + last) // 2
        if alist[mid] == item:
            return True
        elif alist[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    i = random.randint(0, 20)
    list_test = []
    for j in range(10):
        list_test.append(i)
        i += random.randint(0, 20)
    item = list_test[random.randint(0, 9)]
    print(list_test, '要查找的元素:%d' % item)
    result = binary_search(list_test, item)
    print(result)

    print(binary_search_2(list_test, item))
