from collections import defaultdict

class Solution:
    def __init__(self):
        self.seen=[]
    def cycle (self,Graph,curr):
        self.seen.append(curr)
        if not Graph[curr]:
            return
        while Graph[curr]:
            #Graph[curr].remove(curr)
            tmp=Graph[curr].pop()
            Graph[tmp].remove(curr)
            self.cycle(Graph,tmp)
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if n==1:
            return True
        Graph=defaultdict(list)
         
        
        #node=set()
        for i in edges:
            
            #node.update(i)
            Graph[i[0]].append(i[1])
            
            Graph[i[1]].append(i[0])
        if len(Graph)<n:
            return False
        
        self.cycle(Graph,list(Graph.keys())[0])
        if len(self.seen)==n:
            return True
        return False
            
            