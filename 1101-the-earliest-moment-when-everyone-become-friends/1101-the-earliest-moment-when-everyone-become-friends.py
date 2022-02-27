class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x:x[0])
        
        
        def Union(parent,x,y):
            if parent[x]<=parent[y]:
                parent[x]+=parent[y]
                parent[y]=x
            else:
                parent[y]+=parent[x]
                parent[x]=y
        def find(parent,x):
            if parent[x]<0:
                return x
            return find(parent,parent[x])
        
        def union_find(logs,n):
            parent=[-1]*n
            
            for i in logs:
                x=find(parent,i[1])
                y=find(parent,i[2])
                if x!=y:
                    Union(parent,x,y)
                    n-=1
                    if n==1:
                        return i[0]
        time=union_find(logs,n)
        return time if time else -1