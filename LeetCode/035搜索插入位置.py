
def searchInsert(nums, target):
	len_nums = len(nums)
	# if target <= nums[0]:
	# 	return 0
	# if target > nums[len_nums-1]:
	# 	return len_nums
	for i in range(0, len_nums):
		if nums[i] >= target:
			return i
	return len_nums


if __name__ == '__main__':
	nums = [1,3,5,6]
	target = 7
	print(searchInsert(nums, target))