from collections import Counter
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def permute(comb,count):
            if len(comb)==len(nums):
                result.append(list(comb))
                return
            
            for i in count:
                if count[i]>0:
                    comb.append(i)
                    count[i]-=1
                    
                    permute(comb,count)
                    
                    comb.pop()
                    count[i]+=1
                    
        result=[]
        permute([],Counter(nums))
        
        return result