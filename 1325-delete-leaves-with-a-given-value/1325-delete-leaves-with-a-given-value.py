# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def deletednode(root):
            if not root:
                return 
            deletednode(root.right)
            deletednode(root.left)
            if root.left and not root.left.left and not root.left.right and root.left.val==target:
                root.left=None
            if root.right and not root.right.left and not root.right.right and root.right.val==target:
                root.right=None
            return
        
        deletednode(root)
        return None if root.val==target and not root.left and not root.right else root