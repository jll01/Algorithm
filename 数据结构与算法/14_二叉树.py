#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   14_二叉树.py
@Time    :   2019/4/8 20:41:17
@Author  :   LJL
@Version :   1.0
@Email   :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None

'''
# here put the import lib


class Node(object):
    """节点类"""
    def __init__(self, item):
        self.elem = item
        self.lchild = None
        self.rchild = None


class Tree(object):
    """二叉树"""

    def __init__(self):
        # 根节点
        self.root = None

    def add(self, item):

        node = Node(item)

        if self.root is None:
            self.root = node
            return

        queue = [self.root]
        while queue:
            cur_node = queue.pop(0)
            if cur_node.lchild is None:
                cur_node.lchild = node
                return
            else:
                queue.append(cur_node.lchild)

            if cur_node.rchild is None:
                cur_node.rchild = node
                return
            else:
                queue.append(cur_node.rchild)

    def breadth_travel(self):
        """广度遍历"""
        if self.root is None:
            return
        queue = [self.root]

        while queue:
            cur_node = queue.pop(0)
            print(cur_node.elem, end=' ')
            if cur_node.lchild is not None:
                queue.append(cur_node.lchild)

            if cur_node.rchild is not None:
                queue.append(cur_node.rchild)

    def preorder(self, node):
        """前序遍历"""
        if node is None:
            return
        print(node.elem, end=' ')
        self.preorder(node.lchild)
        self.preorder(node.rchild)

    def inorder(self, node):
        """中序遍历"""
        if node is None:
            return
        self.inorder(node.lchild)
        print(node.elem, end=' ')
        self.inorder(node.rchild)

    def postorder(self, node):
        """后序遍历"""
        if node is None:
            return
        self.postorder(node.lchild)
        self.postorder(node.rchild)
        print(node.elem, end=' ')


if __name__ == '__main__':
    tree = Tree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)
    print('二叉树是：', end=' ')
    tree.breadth_travel()
    print(' ')
    print('先序遍历：', end=' ')
    tree.preorder(tree.root)
    print(' ')
    print('中序遍历：', end=' ')
    tree.inorder(tree.root)
    print(' ')
    print('后序遍历：', end=' ')
    tree.postorder(tree.root)
    print(' ')
