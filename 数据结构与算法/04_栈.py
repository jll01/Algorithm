#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   04_栈.py    
@Time    :   2019/4/6 10:24:22
@Author  :   LJL
@Version :   1.0
@Email   :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


class Stack(object):
    """栈"""
    def __init__(self):
        self.__list = []

    def push(self, item):
        """添加栈顶元素"""
        self.__list.append(item)

    def pop(self):
        """删除栈顶元素"""
        return self.__list.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.__list:
            return self.__list[-1]
        else:
            return None

    def is_empty(self):
        """判断栈是否为空"""
        return self.__list == []

    def size(self):
        """栈的长度"""
        return len(self.__list)


if __name__ == '__main__':
    s = Stack()

    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())