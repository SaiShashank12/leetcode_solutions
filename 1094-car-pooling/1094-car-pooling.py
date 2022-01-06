from collections import defaultdict
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        timestamp=defaultdict(int)
        for i in trips:
            timestamp[i[1]]-=i[0]
            timestamp[i[2]]+=i[0]
        # min_start=min(timestamp.keys())
        # max_end=max(timestamp.keys())
        for i in sorted(timestamp.keys()):
            capacity+=timestamp[i]
            if capacity<0:
                return False
        return True
            