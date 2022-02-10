class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        count=0
        sum_group=0
        hash_map={}
        hash_map[0]=1
        for i in range(len(nums)):
            sum_group+=nums[i]
            if sum_group-k in hash_map:
                count+=hash_map.get(sum_group-k)
            hash_map[sum_group]=hash_map.get(sum_group,0)+1
        return count