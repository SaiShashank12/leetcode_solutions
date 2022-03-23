class node:
    def __init__(self):
        self.indegree=[]
        self.out_ward=[]
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph=collections.defaultdict(node)
        for i in zip(recipes,ingredients):
            for j in i[1]:
                graph[j].out_ward.append(i[0])
                graph[i[0]].indegree.append(j)
        for i in graph:
            print("========================")
            print(i)
            print(graph[i].out_ward)
            print(graph[i].indegree)
        result=[]
        while supplies:
            i=supplies.pop(0)
            if i in graph:
                for j in graph[i].out_ward:
                    graph[j].indegree.remove(i)
                    if len(graph[j].indegree)==0:
                        result.append(j)
                        supplies.append(j)
        return result