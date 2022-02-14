from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash_map=defaultdict(int)
        right=10
        left=0
        result=set()
        while right<=len(s):
            hash_map[s[left:right]]+=1
            if hash_map[s[left:right]]>1:
                result.add(s[left:right])
            left+=1
            right+=1
        return list(result)
            