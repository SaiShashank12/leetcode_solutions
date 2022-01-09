class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        t1=t2=0
        for i in range(len(nums)):
            tmp=t1
            t1=max(nums[i]+t2,t1)
            t2=tmp
        return t1
        
        