#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# @File    :   01037有效的回旋镖.py
# @Time    :   2019-05-11 18:47:24
# @Author  :   LJL
# @Version :   1.0
# @Email   :   491692391@qq.com
# @License :   (C)Copyright 2019-2100, LJL
# @Desc    :   None

# here put the import lib


def isBoomerang(points):
	# a = (points[2][1] - points[0][1])/(points[2][0] - points[0][0])
	# b = points[2][1] - a * points[2][0]
	# if points[1][0] * a + b != points[1][1]:
	# 	return True
	# return False
	import math

	x0 = points[0][0]
	y0 = points[0][1]

	x1 = points[1][0]
	y1 = points[1][1]

	x2 = points[2][0]
	y2 = points[2][1]

	a = math.sqrt((x0 - x1)**2 + (y0 - y1)**2)
	b = math.sqrt((x0 - x2)**2 + (y0 - y2)**2)
	c = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


	return a+b>c and a+c>b and c+b>a


if __name__ == '__main__':
	points = [[1,1],[2,3],[3,2]]
	result = isBoomerang(points)
	print(result)

