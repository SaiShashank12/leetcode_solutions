class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        down_one=down_two=0
        for i in range(2,len(cost)+1):
            tmp=down_one
            down_one=min(down_one+cost[i-1],down_two+cost[i-2])
            down_two=tmp
        return down_one