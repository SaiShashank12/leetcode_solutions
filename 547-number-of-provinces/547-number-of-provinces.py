class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(graph,i):
            if i in visited:
                return 
            visited.append(i)
            for j in range(len(graph[i])):
                if i==j or graph[i][j]==0:
                    continue
                dfs(graph,j)
        visited=[]
        provinces=0
        for i in range(len(isConnected)):
            if i in visited:
                continue
            provinces+=1
            dfs(isConnected,i)
        return provinces
                