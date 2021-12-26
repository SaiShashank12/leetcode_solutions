# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root): return root
        l, r = root.left, root.right
        root.left = root.right = None
        while(l):
            ll, lr, lself = l.left, l.right, l
            l.left, l.right = r, root
            root = l
            l, r = ll, lr
        return root