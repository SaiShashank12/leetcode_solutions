# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:
from functools import lru_cache
class Solution:
    @lru_cache(maxsize=None)
    def cachedKnows(self,a,b):
        return knows(a,b)
    def findCelebrity(self, n: int) -> int:
        self.n=n
        candidate_celb=0
        for i in range(1,n):
            if self.cachedKnows(candidate_celb,i):
                candidate_celb=i
        if self.is_know(candidate_celb):
            return candidate_celb
        return -1
    def is_know(self,i):
        for j in range(self.n):
            if i==j:continue
            if self.cachedKnows(i,j) or not self.cachedKnows(j,i):
                return False
        return True