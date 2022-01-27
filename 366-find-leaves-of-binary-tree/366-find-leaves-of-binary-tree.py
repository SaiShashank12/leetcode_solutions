# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        def leafDelete(root):
            if root == None:
                return None
            if root.left == None and root.right == None:
                deleted_list.append(root.val)
                return None

            # Else recursively delete in left
            # and right subtrees.
            root.left = leafDelete(root.left)
            root.right = leafDelete(root.right)

            return root
        deleted_list=[]
        result=[]
        while root:
            root=leafDelete(root)
            print(deleted_list)
            result.append(deleted_list)
            deleted_list=[]
        return result