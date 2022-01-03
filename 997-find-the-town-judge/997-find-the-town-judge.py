class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        Graph=[set() for i in range(n)]
        for i in trust:
            Graph[i[0]-1].add(i[1]-1)
        candidate_judge=-1
        for i in range(len(Graph)):
            if not Graph[i]:
                candidate_judge=i
        for j in range(len(Graph)):
            if j!=candidate_judge and candidate_judge not in Graph[j]:
                return -1
        return candidate_judge+1