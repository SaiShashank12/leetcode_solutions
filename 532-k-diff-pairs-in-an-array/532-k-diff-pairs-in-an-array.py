class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        count=0
        seen=[]
        nums.sort()
        for i in range(len(nums)):
            result=k+nums[i]
            if result in nums[i+1:] and [nums[i],result] not in seen:
                count+=1
                seen.append([nums[i],result])
        return count
                