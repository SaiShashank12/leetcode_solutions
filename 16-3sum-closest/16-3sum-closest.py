class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        bts=999
        g=0
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            k=target-nums[i]
            
            while left<right:
                result=nums[left]+nums[right]
                if bts>abs(k-result):
                    bts=abs(k-result)
                    g=nums[i]+nums[left]+nums[right]
                if k==result:
                    return g
                if k<result:
                    right-=1
                else:
                    left+=1
                
        return g 
                    
                    