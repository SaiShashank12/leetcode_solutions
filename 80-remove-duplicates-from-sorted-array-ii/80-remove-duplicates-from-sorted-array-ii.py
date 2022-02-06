#from collections import Counter
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr=None
        count=0
        i=0
        while i<len(nums):
            
            if  curr==None or curr!=nums[i]:
                curr=nums[i]
                count=1
                i+=1
                continue
            if curr==nums[i]:
                count+=1
            if count>2:
                nums.pop(i)
                continue
            i+=1
        return len(nums)
            