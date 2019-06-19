
def myAtoi(str_strip):
	# num = list(str(i) for i in range(10))
	str_strip = str_strip.strip(' ')
	if len(str_strip) == 1 and str_strip in ['-', '+'] or len(str_strip) == 0:
		return 0	
	str_num = str_strip[1:] if str_strip[0] == '-' or str_strip[0] == '+' else str_strip
	result = '-' if str_strip[0] == '-' else ''
	if ord(str_num[0]) <48 or ord(str_num[0])>57:
		return 0	
	for i in range(len(str_num)):
		if 48 <= ord(str_num[i]) <= 57:
			result = "%s%s"%(result,str_num[i])
		else:
			break
	# result = flag*int(''.join(list_num))

	result = int(result)
	if -2**31 > result:
		return -2**31
	elif result > 2**31-1:
		return 2**31-1
	return result

if __name__ == '__main__':
 	result = myAtoi("  236df5  ")
 	print(result)