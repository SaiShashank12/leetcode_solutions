# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        self.n=n
        candidate_celb=0
        for i in range(1,n):
            if knows(candidate_celb,i):
                candidate_celb=i
        if self.is_know(candidate_celb):
            return candidate_celb
        return -1
    def is_know(self,i):
        for j in range(self.n):
            if i==j:continue
            if knows(i,j) or not knows(j,i):
                return False
        return True