def twoSum(nums, target):
	for i in range(len(nums)):
		for j in range(len(nums)):
			if i!=j:
				if nums[i]==nums[j]:
					return [i,j]