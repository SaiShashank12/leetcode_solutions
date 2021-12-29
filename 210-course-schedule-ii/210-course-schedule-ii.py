from collections import defaultdict
class node:
    def __init__(self):
        self.val=[]
        self.count=0
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
#         if not prerequisites and numCourses>0:
#             return [i for i in reversed(range(numCourses))]
        
        Graph=defaultdict(node)
        for i in range(numCourses):
            Graph[i]
        for i in prerequisites:
            #Graph[i[0]].val.append(i[1])
            Graph[i[1]].val.append(i[0])
            Graph[i[0]].count+=1
        
            
        startnodes=[]
        for k,v in Graph.items():
            if not v.count:
                startnodes.append(k)
        result=[]
        while startnodes:
            tmp=startnodes.pop(0)
            result.append(tmp)
            for i in Graph[tmp].val:
                Graph[i].count-=1
                if Graph[i].count==0:
                    startnodes.append(i)
        return result if len(result)==numCourses else []
                    
                