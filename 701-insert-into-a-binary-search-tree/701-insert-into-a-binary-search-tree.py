# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rec_bst(self,root,val):
        if not root:
            return TreeNode(val)
        if root.val<val:
            root.right=self.rec_bst(root.right,val)
        else:
            root.left=self.rec_bst(root.left,val)
        return root
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.rec_bst(root,val)