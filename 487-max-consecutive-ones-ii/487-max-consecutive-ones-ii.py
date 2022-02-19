class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        right=left=0
        stack=[]
        longest=0
        num_ones=sum(nums)
        num_zero=0
        while right<len(nums):
            if nums[right]==0 and not stack:
                stack.append(right)
            elif nums[right]==0 and stack:
                left=stack.pop()+1
                stack.append(right)
                longest=max(longest,right-left)
            
            longest=max(longest,right-left+1)
            right+=1
            
                
            
        
        return longest