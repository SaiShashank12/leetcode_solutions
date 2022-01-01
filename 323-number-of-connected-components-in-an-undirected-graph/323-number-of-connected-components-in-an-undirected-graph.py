class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        Graph=[set() for _ in range(n)]
        for i in edges:
            Graph[i[0]].add(i[1])
            Graph[i[1]].add(i[0])
        visit=[]
        count=0
        for i in range(len(Graph)):
            if i in visit:
                continue
            queue=[i]
            count+=1
            while queue:
                tmp=queue.pop(0)
                if tmp not in visit:
                    visit.append(tmp)
                else:
                    continue
                queue.extend(list(Graph[tmp]))
        return count
            
        