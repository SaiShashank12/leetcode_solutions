from collections import OrderedDict

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        basket=OrderedDict()
        max_tree=0
        right=left=0
        for i,v in enumerate(fruits):
            if v in basket:
                del basket[v]
            basket[v]=i
            right+=1
            if len(basket)==3:
                _,del_idx=basket.popitem(last=False)
                left=del_idx+1
            max_tree=max(max_tree,right-left)
            
        return max_tree