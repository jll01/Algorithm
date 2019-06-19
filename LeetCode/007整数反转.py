
def my_reverse(x):
	if x>=0:
		flag = 1
	else:
		flag = -1

	list_x = list(str(flag*x))	
	len_x = len(list_x)
	for i in range(len_x-1):
		list_x.append(list_x.pop(-2-i))
	result = int(''.join(list_x))*flag
	if -1*2**31 <= result <= 2**31:
		return result
	else:
		return 0

if __name__ == '__main__':
 	x = 120
 	result = my_reverse(x)
 	print(result)
 	# print(2**31-1)
 	# print(-2**31)
