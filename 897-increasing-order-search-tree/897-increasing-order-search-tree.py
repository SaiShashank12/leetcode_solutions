# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(root):
            return inorder(root.left)+[root.val]+inorder(root.right) if root else []
        def line_increase(root,i):
            root=TreeNode(i)
        result_list=inorder(root)
        tmpr=TreeNode()
        tmp=tmpr
        
        for i in result_list:
            tmp.right=TreeNode(i)
            tmp=tmp.right
        return tmpr.right