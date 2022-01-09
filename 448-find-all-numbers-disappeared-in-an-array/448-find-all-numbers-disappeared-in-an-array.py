from collections import Counter
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        unique=set(nums)
        n=len(nums)
        arr=[i for i in range(1,n+1)]
        
        return [item for item in arr if item not in unique]