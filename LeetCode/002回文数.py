#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   002回文数.py
@Time    :   2019/05/06 18:13:33
@Author  :   LJL
@Version :   1.0
@Contact :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None
'''
# here put the import lib

def isPalindrome(num):
    # for i in range(int(len(num)/2)):
    #     if num[i] != num[-1-i]:
    #         return 'false'
    #     else:
    #         flag = True
    # if flag:
    #     return 'true'
    num_re = num[::-1]
    if num_re == num:
        return True
    else:
        return False


if __name__ == '__main__':
    num = 12321321
    result = isPalindrome(str(num))
    print(result)