class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        count=0
        for i in range(len(nums)-1,0,-1):
            count+=nums[i]-nums[0]
            
        return count