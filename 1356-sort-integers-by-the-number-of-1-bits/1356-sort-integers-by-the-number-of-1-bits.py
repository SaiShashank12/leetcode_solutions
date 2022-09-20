class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        det=[[i,bin(i).count('1')] for i in arr]
        tmp=sorted(det,key=lambda x:(x[1],x[0]))
        
        return [i[0] for i in tmp]