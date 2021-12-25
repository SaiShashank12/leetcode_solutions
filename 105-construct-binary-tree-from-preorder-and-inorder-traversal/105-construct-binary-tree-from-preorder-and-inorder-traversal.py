# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def helper(left,right):
            nonlocal preorder_index
            if left>right:
                return None
            root_value=preorder[preorder_index]
            root=TreeNode(root_value)
            preorder_index+=1
            root.left=helper(left,inorder_index[root_value]-1)
            root.right=helper(inorder_index[root_value]+1,right)
            
            return root
        preorder_index=0
        
        inorder_index={v:i for i,v in enumerate(inorder)}
        
        return helper(0,len(preorder)-1)