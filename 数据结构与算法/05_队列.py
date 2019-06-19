#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   05_队列.py
@Time    :   2019/4/6 10:42:42
@Author  :   LJL
@Version :   1.0
@Email   :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


class Queue(object):
    """队列，先进先出"""
    def __init__(self):
        self.__list = []

    def inqueue(self, item):
        """添加队列元素"""
        self.__list.append(item)

    def outqueue(self):
        """删除队列元素"""
        return self.__list.pop(0)

    def is_empty(self):
        """判断是否为空"""
        return self.__list == []

    def size(self):
        """队列元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    q = Queue()

    q.inqueue(1)
    q.inqueue(2)
    q.inqueue(3)
    q.inqueue(4)

    print(q.outqueue())
    print(q.outqueue())
    print(q.outqueue())
    print(q.outqueue())
