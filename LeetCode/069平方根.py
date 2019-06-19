 
def mySqrt(x):
	left = 0
	right = x
	while left <= right:		
		mid = (left + right)//2
		if mid**2 > x:
			right = mid - 1
		elif mid**2 < x:
			left = mid + 1
		else:
			return mid
	return right
 

if __name__ == '__main__':
	result = mySqrt(-1)
	print(result)