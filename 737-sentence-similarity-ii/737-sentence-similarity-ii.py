class Solution:
    def areSentencesSimilarTwo(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1)!=len(sentence2):
            return False
        
        def find(parent,x):
            if parent.get(x,-1)==-1:
                return x
            return find(parent,parent[x])
        def Union(parent,x,y):
            parent[x]=y
        def find_union(similarPairs):
            for x,y in similarPairs:
                x=find(parent,x)
                y=find(parent,y)
                if x!=y:
                    Union(parent,x,y)
        parent={}         
        find_union(similarPairs)
        print(parent)
        
        for a,b in zip(sentence1,sentence2):
            x=find(parent,a)
            y=find(parent,b)
            if x!=y:
                return False
        return True