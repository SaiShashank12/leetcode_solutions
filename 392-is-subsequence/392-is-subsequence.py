
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        j=0
        if not s:
            return True
        if not t:
            return False
        for i in t:
            if s[j]==i:
                j+=1
            if len(s)==j:
                return True
        return False