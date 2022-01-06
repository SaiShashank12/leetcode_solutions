from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        start=defaultdict(int)
        end=defaultdict(int)
        for i in trips:
            start[i[1]]+=i[0]
            end[i[2]]+=i[0]
        min_start=min(start.keys())
        max_end=max(end.keys())
        for i in range(min_start,max_end):
            capacity+=end[i]
            capacity-=start[i]
            if capacity<0:
                return False
        return True
            