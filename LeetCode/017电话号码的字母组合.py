#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   017电话号码的字母组合.py
# @Time    :   2019-05-15 18:07:19
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def letterCombinations(digits):
        if '1' in list(digits) or '0' in list(digits) or not digits :
        	return []
        letter = {
        	'2': 'abc', 
        	'3': 'def', 
        	'4': 'ghi', 
        	'5': 'jkl',
			'6': 'mno', 
			'7': 'pqrs', 
			'8': 'tuv', 
			'9': 'wxyz',
		}

        n = len(digits)
        res = ['']
        for i in range(n):
            res = [x + y for x in res for y in letter[digits[i]]]
        return res



if __name__ == '__main__':
	digits = '23'
	result = letterCombinations(digits)
	print(result)