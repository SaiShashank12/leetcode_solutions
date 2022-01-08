class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        result=0
        for i in range(0,len(arr)):
            pick = 2*i+1
            for j in range(0,len(arr)):
                if j+pick>len(arr):
                    break
                result+=sum(arr[j:j+pick])
        return result