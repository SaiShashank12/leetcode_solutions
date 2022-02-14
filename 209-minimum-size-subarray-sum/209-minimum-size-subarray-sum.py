class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left=right=0
        prefix_sum=0
        min_length=9999
        while right<len(nums):
            prefix_sum+=nums[right]
            right+=1
            
            
            while prefix_sum>=target:
                min_length=min(min_length,right-left)
                prefix_sum-=nums[left]
                left+=1
                
        return min_length if min_length<9999 else 0