class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        right=left=0
        stack=[]
        longest=0
        num_ones=sum(nums)
        num_zero=0
        while right<len(nums):
            if nums[right]==0:
                num_zero+=1
            while num_zero==2:
                if nums[left]==0:
                    num_zero-=1
                left+=1
            longest=max(longest,right-left+1)
            right+=1
            
                
            
        
        return longest