#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   11_快速排序.py    
@Time    :   2019/4/8 10:16:22
@Author  :   LJL
@Version :   1.0
@Email :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


import random


def quick_sort(alist, first, last):
    '''快速排序'''

    if first >= last:
        return

    # 以每次的第一个元素为中间值，将列表分为大小两组
    mid_value = alist[first]
    low = first
    high = last

    # 当每个列表的开始和结束下标值满足low<high时，执行下列语句
    while low < high:
        while low < high and alist[high] >= mid_value:
            high -= 1
        # 当不满足上面条件时，将高位指向的值赋给低位，即交换高位和低位下标对应的值
        alist[low] = alist[high]

        while low < high and alist[low] < mid_value:
            low += 1
        alist[high] = alist[low]

    alist[low] = mid_value

    quick_sort(alist, first, low-1)
    quick_sort(alist, low+1, last)


if __name__ == '__main__':
    list_test = [random.randint(0, 100) for i in range(random.randint(8, 15))]
    print('原来的列表:\t{}'.format(list_test))
    print('sorted排序:\t{}'.format(sorted(list_test)))
    quick_sort(list_test, 0, len(list_test)-1)
    print('自定义排序:\t{}'.format(list_test))
