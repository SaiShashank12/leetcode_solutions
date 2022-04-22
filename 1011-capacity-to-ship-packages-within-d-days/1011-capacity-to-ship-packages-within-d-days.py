class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasiable(capacity):
            total=0
            day=1
            
            for i in weights:
                total+=i
                
                if total>capacity:
                    day+=1
                    total=i
                    
                    if day>days:
                        return False
            return True
        
        
        left,right=max(weights),sum(weights)
        
        while left<right:
            
            mid=(left+right)//2
            
            if feasiable(mid):
                right=mid
            else:
                left=mid+1
                
        return left