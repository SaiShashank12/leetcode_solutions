class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        merge=[]
        for i in intervals:
            if not merge or merge[-1][1]<i[0]:
                merge.append(i)
                continue
            merge[-1][1]=max(merge[-1][1],i[1])
        return merge