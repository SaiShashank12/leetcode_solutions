class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_wealth=0
        for i in accounts:
            tmp=sum(i)
            if max_wealth<tmp:
                max_wealth=tmp
        return max_wealth