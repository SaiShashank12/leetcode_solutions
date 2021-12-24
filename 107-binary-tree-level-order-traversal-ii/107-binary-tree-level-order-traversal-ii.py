# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        level=[]
        next_level=deque([root])
        
        while root and next_level:
            curr_level=next_level
            next_level=deque()
            level.append([])
            
            for node in curr_level:
                level[-1].append(node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
        return level[::-1]