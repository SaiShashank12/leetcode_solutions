class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left=0
        right=0
        set_result=set()
        len_result=0
        while right<len(s):
            
            
            right+=1
            while len(set(s[left:right]))>k:
                left+=1
                
            else:
                len_result=max(len_result,right-left)
        return len_result
            
            