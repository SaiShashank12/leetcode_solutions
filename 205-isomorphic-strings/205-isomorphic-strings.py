class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        result1={}
        result2={}
        for i in range(len(s)):
            if s[i] in result1  and result1[s[i]]!=t[i]:
                return False 
            if t[i] in result2 and result2[t[i]]!=s[i]:
                return False
            result1[s[i]]=t[i]
            result2[t[i]]=s[i]
        return True