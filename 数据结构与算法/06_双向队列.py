#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   06_双向队列.py    
@Time    :   2019/4/6 10:49:46
@Author  :   LJL
@Version :   1.0
@Email   :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


class Deque(object):
    """双向队列"""
    def __init__(self):
        self.__list = []

    def add_front(self, item):
        """头部插入元素"""
        self.__list.insert(0, item)

    def add_rear(self, item):
        """尾部添加元素"""
        self.__list.append(item)

    def pop_front(self):
        """头部删除元素"""
        return self.__list.pop(0)

    def pop_rear(self):
        """尾部删除元素"""
        return self.__list.pop()

    def is_empty(self):
        """判断是否为空"""
        return self.__list == []

    def size(self):
        """判断队列元素个数"""
        return len(self.__list)


if __name__ == '__main__':
    q = Deque()

    q.add_front(1)
    q.add_front(2)
    q.add_front(3)
    q.add_front(4)

    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_front())
    print(q.pop_front())

