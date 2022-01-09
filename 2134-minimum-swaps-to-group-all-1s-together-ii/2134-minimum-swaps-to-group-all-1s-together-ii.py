class Solution:
	def minSwaps(self, nums: List[int]) -> int:
		cntOne = nums.count(1)
		cntZero = len(nums) - cntOne
		res = len(nums)
		one = nums[:cntOne].count(1)
		zero = nums[:cntZero].count(0)
		for i in range(cntOne, len(nums)):
			if nums[i] == 1:
				one += 1
			if nums[i - cntOne] == 1:
				one -= 1
			res = min(res, cntOne - one)
		for i in range(cntZero, len(nums)):
			if nums[i] == 0:
				zero += 1
			if nums[i - cntZero] == 0:
				zero -= 1
			res = min(res, cntZero - zero)    
		return res