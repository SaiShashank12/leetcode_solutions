
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash_map=set()
        right=10
        left=0
        result=set()
        while right<=len(s):
            if s[left:right] in hash_map:
                result.add(s[left:right])
            hash_map.add(s[left:right])
            
            left+=1
            right+=1
        return list(result)
            