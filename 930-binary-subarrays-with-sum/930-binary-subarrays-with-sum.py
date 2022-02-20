class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix_sum=0
        hash_map={0:1}
        count=0
        for i in nums:
            prefix_sum+=i
            if prefix_sum-goal in hash_map:
                count+=hash_map[prefix_sum-goal]
            hash_map[prefix_sum]=hash_map.get(prefix_sum,0)+1
        return count
            