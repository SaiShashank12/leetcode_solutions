class Solution:
    def traversal(self, g, visited, v):
        visited.add(v)
        
        for neigb in g[v]:
            if neigb not in visited:
                self.traversal(g, visited, neigb)
                
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        
        g=[set() for _ in range(n)]
        for i in edges:
            g[i[0]].add(i[1])
            g[i[1]].add(i[0])
        visited = set()
        res = 0
        for v in range(n):
            if v not in visited:
                res += 1
                self.traversal(g, visited, v)
        
        return res