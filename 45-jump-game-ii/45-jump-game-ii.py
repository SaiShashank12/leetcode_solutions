class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        import sys
        @lru_cache(None)
        def helper(idx):
            if idx==n-1:
                return 0
            if idx+nums[idx]>=n-1:
                return 1
            ans=sys.maxsize
            
            for i in range(1,nums[idx]+1):
                ans=min(ans,1+helper(idx+i))
            
            return ans
        
        return helper(0)