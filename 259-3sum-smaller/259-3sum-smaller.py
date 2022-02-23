class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        
        count=0
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                if nums[i]+nums[left]+nums[right]<target:
                    count+=right-left
                    left+=1
                else:
                    right-=1
        return count
                    
            