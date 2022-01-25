# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def findNearestRightNode(self, root: TreeNode, u: TreeNode) -> Optional[TreeNode]:
        current_lvl=deque([])
        next_level=deque([root,])
        while next_level:
            current_lvl=next_level
            next_level=deque()
            while current_lvl:
                root=current_lvl.popleft()

                if root==u:
                    return current_lvl.popleft() if current_lvl else None
                if root.left:
                    next_level.append(root.left)
                if root.right:
                    next_level.append(root.right)
        
            
        return None