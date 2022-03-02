class Solution:
    def generateSentences(self, synonyms: List[List[str]], text: str) -> List[str]:
        graph={}
        
        def union(x,y):
            graph[find(x)]=find(y)
            
        def find(x):
            graph.setdefault(x,x)
            if graph[x]!=x:
                graph[x]=find(graph[x])
            return graph[x]
        
        for a,b in synonyms:
            union(a,b)
        
        
        d=collections.defaultdict(set)
        for a,b in synonyms:
            root=find(a)
            d[root]|=set([a,b])
        
        #print(d)
        #print(graph)
        result=[]
        for i in text.split():
            if i not in graph:
                result.append([i])
            else:
                r=find(i)
                #print(r)
                result.append(list(d[r]))
        fin_res = [" ".join(sentence) for sentence in itertools.product(*result)]
        return sorted(fin_res)       