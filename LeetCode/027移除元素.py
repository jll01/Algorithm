
def removeElement(nums, val):
	if val in nums:
		while True:
			nums.remove(val)
			# if val in nums:
			# 	nums[nums.index(val)] = ''
			# 	print(nums)
			if val not in nums:
				break 
	return len(nums)


if __name__ == '__main__':
	nums = [3,2,2,3]
	val = 3
	result = removeElement(nums, val)
	print(result)