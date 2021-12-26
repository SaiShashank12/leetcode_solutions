"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        next_level=[root]
        result=[]
        while(next_level):
            result.append([i for i in next_level])
            current_level=next_level
            next_level=[]
            while current_level:
                tmp=current_level.pop(0)
                if tmp.left:
                    next_level.append(tmp.left)
                if tmp.right:
                    next_level.append(tmp.right)
        for i in result:
            curr=i[0]
            for j in range(1,len(i)):
                curr.next=i[j]
                curr=curr.next
            curr.next=None
            
        return root