class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        count=0
        def find(parent,x):
            if parent[x]<0:
                return x
            return find(parent,parent[x])
        def union(parent,x,y):
            if parent[x]<=parent[y]:
                parent[x]+=parent[y]
                parent[y]=x
            else:
                parent[y]+=parent[x]
                parent[x]=y
                
        def find_union(edges,parent,path):
            nonlocal count
            e=0
            for i in edges:
                if i[0]==path:
                    
                    x=find(parent,i[1])
                    y=find(parent,i[2])
                    if x==y:
                        count+=1
                        continue
                    union(parent,x,y)
                    e+=1
                
            return parent,e
                
        parent_everyone,e=find_union(edges,[-1]*(n+1),3)
        print(count)
        
        bob_parent,e1=find_union(edges,parent_everyone.copy(),2)
        alex_parent,e2=find_union(edges,parent_everyone.copy(),1)
        # if e1!= alex_parent:
        #     return -1
        e1+=e
        e2+=e
        return count if e1==e2==n-1 else -1
       