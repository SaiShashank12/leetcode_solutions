index=""
class Trienode:
    def __init__(self):
        
        self.children={}
        self.isLeaf=False
class Solution:
    def __init__(self):
        self.root=Trienode()
    def contructTrie(self,strs):
        for i in strs:
            tmp_root=self.root
            for j in i:
                if j not in tmp_root.children:
                    tmp_root.children[j]=Trienode()
                tmp_root=tmp_root.children[j]
            tmp_root.isLeaf=True
    def count_children(self,node):
        count=0
        for i in node.children.keys():
            count+=1
            global index
            index=i
        return count
    def walk_trie(self):
        pcrawl=self.root
        prefix=""
        while(self.count_children(pcrawl)==1 and pcrawl.isLeaf==False):
            pcrawl=pcrawl.children[index]
            prefix+=index
        return prefix
    def longestCommonPrefix(self, strs: List[str]) -> str:
        self.contructTrie(strs)   
        return self.walk_trie()
        