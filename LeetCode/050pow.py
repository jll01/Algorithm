#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   050pow.py
@Time    :   2019/05/06 21:57:34
@Author  :   LJL
@Version :   1.0
@Contact :   491692391@qq.com
@License :   (C)Copyright 2019-2100, LJL
@Desc    :   None
'''
# here put the import lib



def myPow(x, n):
    if n < 0:
        x = 1/x
        n = -n
    if n == 0 or x == 1:
        return 1
    if n == 1:
        return x
    if n % 2 == 0:
        return myPow(x*x, n/2)
    else:
        return myPow(x*x, n//2)*x    

    # ans=1
    # i=abs(n)
    # while i != 0 :
    #     if i % 2 != 0:
    #         ans*=x
    #     x*=x
    #     i//=2       
    
    # return ans if n>0 else 1/ans


if __name__ == '__main__':
    a = myPow(2, 10)
    print(a)
