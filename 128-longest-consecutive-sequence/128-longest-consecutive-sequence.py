class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        count=max_count=1
        
        non_duplicate=list(set(nums))
        non_duplicate.sort()
        for i in range(len(non_duplicate)-1):
            if non_duplicate[i]+1!=non_duplicate[i+1]:
                count=0
            count+=1
            max_count=max(count,max_count)
        return max_count