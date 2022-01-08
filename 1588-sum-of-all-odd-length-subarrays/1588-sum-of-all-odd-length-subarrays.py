class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        # Brute Force O(n^3)
        # Alternative O(n). Given the length n of arr, how many times will arr[k] appear in the total sum?
        
        res = 0
        for i in range(len(arr)):
            res += ((i + 1) * (len(arr) - i) + 1) // 2 * arr[i]
        return res