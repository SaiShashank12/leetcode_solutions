class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        
        
        parent={}
        
        def Union(x,y):
            parent[find(x)]=find(y)
            
        def find(x):
            parent.setdefault(x,x)
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]
        
        for i in pairs:
            Union(i[0],i[1])
        print(parent)
        
        d=collections.defaultdict(list)
        
        for i in range(len(s)):
            d[find(i)].append(s[i])
        for comp_id in d.keys(): 
            d[comp_id].sort(reverse=True)
            
        print(d)
        
        res=[]
        for i in range(len(s)): 
            res.append(d[find(i)].pop())
        return "".join(res)