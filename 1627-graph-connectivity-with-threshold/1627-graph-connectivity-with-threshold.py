class Solution:
    def areConnected(self, n: int, threshold: int, queries: List[List[int]]) -> List[bool]:
        if threshold == 0: return [True] * len(queries)
        if threshold >= n / 2: return [False] * len(queries)

        parent={}
        def common_divisor(x,y,k):
            
            for i in range(1,min(x,y)+1):
                
                if x%i==0 and y%i==0 and i>k:
                    return True
                    
            return False
        
        def find(x):
            parent.setdefault(x,x)
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        def union(x,y,k):
            if common_divisor(x,y,k):
                parent[find(x)]=find(y)
        for z in range(threshold + 1, n + 1):
            for x in range(z + z, n + 1, z):
                union(z,x,threshold)
                
        result=[]
        for i in queries:
            if find(i[0])==find(i[1]):
                result.append(True)
            else:
                result.append(False)
        return result
        
                