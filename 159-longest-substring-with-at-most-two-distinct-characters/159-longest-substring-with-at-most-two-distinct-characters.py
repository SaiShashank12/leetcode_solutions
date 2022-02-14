class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left=right=0
        max_size=cnt_char=0
        while right<len(s):
            right+=1
            
            if len(set(s[left:right]))>2:
                left+=1
            elif len(set(s[left:right]))<=2:
                max_size=max(right-left,max_size)
        return max_size