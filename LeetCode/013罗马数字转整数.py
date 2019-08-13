
# 罗马数字与整数的关系
str_dict = {
	'I': 1,
	'V': 5,
	'X': 10,
	'L': 50,
	'C': 100,
	'D': 500,
	'M': 1000,
}

def romanToInt(str_num):
  '''转换，前一个小于后一个，则相当于后一个加上前面的值的负数'''
	list_num = []
	s = 0
	for i in range(len(str_num)):
		if i < len(str_num)-1 and str_dict[str_num[i]] < str_dict[str_num[i+1]]:
			list_num.append(-1 * str_dict[str_num[i]]) 
			s -= str_dict[str_num[i]]
		else:
			list_num.append(str_dict[str_num[i]])
			s += str_dict[str_num[i]]
			
	print(list_num) 
	return s
	


if __name__ == '__main__':

	a = 'XIXIVM'
	res = romanToInt(a)
	print(res)
