#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   09_插入排序.py    
@Time    :   2019/4/7 20:34:55
@Author  :   LJL
@Version :   1.0
@Email :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


import random


def insert_sort(alist):
    for i in range(1, len(alist)):
        for j in range(i, 0, -1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j-1] = alist[j-1], alist[j]

    return alist



if __name__ == '__main__':
    list_test = [random.randint(0,100) for i in range(random.randint(8,15))]
    print('原来的列表:\t{}'.format(list_test))
    print('sorted排序:\t{}'.format(sorted(list_test)))
    insert_list = insert_sort(list_test)
    print('自定义排序:\t{}'.format(list_test))
