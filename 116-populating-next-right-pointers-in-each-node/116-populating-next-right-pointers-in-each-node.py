"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return root
        Q=deque([root])
        while Q:
            size=len(Q)
            for i in range(size):
                tmp=Q.popleft()
                if i<size-1:
                    tmp.next=Q[0]
                if tmp.left:
                    Q.append(tmp.left)
                if tmp.right:
                    Q.append(tmp.right)
        return root