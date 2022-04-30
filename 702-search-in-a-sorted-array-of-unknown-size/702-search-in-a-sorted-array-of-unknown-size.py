# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:

class Solution:
    def search(self, reader: 'ArrayReader', target: int) -> int:
        mid=target-reader.get(0)
        
        if reader.get(mid)==target:
            return mid
        left,right=0,mid
        
        while left<right:
            mid=(left+right)//2
            
            if reader.get(mid)==target:
                return mid
            if reader.get(mid)>target:
                right=mid
            else:
                left=mid+1
           
            
        return -1