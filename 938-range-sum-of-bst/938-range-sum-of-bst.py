# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        def helper(root,low,high):
            nonlocal result_sum
            if not root:
                return 
            if root.val<low:
                helper(root.right,low,high)
            if root.val>high:
                helper(root.left,low,high)
            if root.val>=low and root.val<=high:
                result_sum+=root.val
                helper(root.right,low,high)
                helper(root.left,low,high)
        result_sum=0
        helper(root,low,high)
        return result_sum
        