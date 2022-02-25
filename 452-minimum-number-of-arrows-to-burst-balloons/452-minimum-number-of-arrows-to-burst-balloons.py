class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        merge=[]
        for i in points:
            if not merge or merge[-1][1]<i[0]:
                merge.append(i)
                continue
            merge[-1][1]=min(merge[-1][1],i[1])
        return len(merge)