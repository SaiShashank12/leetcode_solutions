class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent=[-1]*26
        
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
        for i in equations:
            if i[1]=="=":
                x=find(parent,ord(i[0])-ord('a'))
                y=find(parent,ord(i[-1])-ord('a'))
                if x!=y:
                    union(parent,x,y)
        for i in equations:
            if i[1]=="!":
                x=find(parent,ord(i[0])-ord('a'))
                y=find(parent,ord(i[-1])-ord('a'))
                if x==y:
                    return False
        return True
        
        
                