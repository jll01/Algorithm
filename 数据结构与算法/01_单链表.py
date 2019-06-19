#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   01_单链表.py
@Time    :   2019/4/6 11:29:06
@Author  :   LJL
@Version :   1.0
@Email   :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


class Node(object):
    """节点"""
    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SingleLinkList(object):
    """单链表"""

    def __init__(self, node=None):
        self.__head = node

    def is_empty(self):
        """判断链表是否为空"""
        return self.__head == None

    def length(self):
        """返回链表长度"""
        # cur用来移动遍历节点
        cur = self.__head
        # count记录数量
        count = 0

        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head

        while cur != None:
            print(cur.elem, end=" ")
            cur = cur.next
        print("")

    def add(self, item):
        """链表头部添加元素，头插法"""
        node = Node(item)
        node.next = self.__head
        self.__head = node

    def append(self, item):
        """链表尾部添加元素, 尾插法"""
        node = Node(item)

        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        """指定位置添加元素
        pos 从0开始
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0

            while count < (pos-1):
                count += 1
                pre = pre.next
            # 当循环退出后，pre指向pos-1位置
            node = Node(item)
            node.next = pre.next
            pre.next = node

    def remove(self, item):
        """删除节点"""
        cur = self.__head
        pre = None

        while cur != None:
            if cur.elem == item:
                if cur == self.__head:
                    self.__head = cur.next
                else:
                    pre.next = cur.next
                break
            else:
                pre = cur
                cur = cur.next

    def search(self, item):
        """查找节点"""
        cur = self.__head

        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False



if __name__ == "__main__":
    ll = SingleLinkList()
    print(ll.is_empty())
    print(ll.length())

    ll.append(1)
    print(ll.is_empty())
    print(ll.length())


    ll.append(2)
    ll.add(8)
    ll.append(3)
    ll.append(4)
    ll.append(5)
    ll.append(6)

    ll.insert(-1, 9)
    ll.travel()
    ll.insert(3, 12)
    ll.travel()
    ll.insert(10, 12)
    ll.travel()
    ll.remove(12)
    ll.travel()
    ll.remove(9)
    ll.travel()
    ll.remove(13)
    ll.travel()

