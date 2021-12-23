class Solution:
    
        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index= {}
        output = []
        for i,e in enumerate(nums):
            diff = target - e
            if diff in index:
                output.append(i)
                output.append(index[diff])
                break
            else:
                index[e]=i
        return output