
def strStr(haystack, needle):
	if not needle.strip(' '):
		return 0
	str_res = haystack.split(needle)
	if len(str_res)==1:
		return -1
	return len(str_res[0])


if __name__ == '__main__':
	haystack =  "aaaaa"
	needle = "bba"
	result = strStr(haystack, needle)
	print(result)

