class Solution:
    def traversal(self, g, visited, v):
        visited.add(v)
        
        for neigb in g[v]:
            if neigb not in visited:
                self.traversal(g, visited, neigb)
                
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
        
        g = collections.defaultdict(list)
        visited = set()
        
        for (e1,e2) in edges:
            g[e1].append(e2)
            g[e2].append(e1)
        
        res = 0
        for v in range(n):
            if v not in visited:
                res += 1
                self.traversal(g, visited, v)
        
        return res