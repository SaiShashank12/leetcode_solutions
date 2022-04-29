# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        def helper():
            left,right=0,binaryMatrix.dimensions()[1]-1
            last=binaryMatrix.dimensions()[1]
            while left<=right:
                mid=(left+right)//2
                for i in range(binaryMatrix.dimensions()[0]):
                    if binaryMatrix.get(i,mid)==1 and last>mid:
                        last=mid
                        right=mid-1
                        break
                if right!=mid-1:
                    left=mid+1
            return last if last<binaryMatrix.dimensions()[1] else -1
        return helper()