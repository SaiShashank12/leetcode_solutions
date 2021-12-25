# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        def Sum_path(root,target,result):
            
            if not root:
                #result.pop()
                return 
            target-=root.val
            result.append(root.val)
            if target==0 and not root.left and not root.right:
                ret=[i for i in result]
                Compelet_result.append(ret)
                result.pop()
                return 
            
            if root.left:
                
                Sum_path(root.left,target,result)
            if root.right:
                Sum_path(root.right,target,result)
            
            result.pop() 
        Compelet_result=[]
        Sum_path(root,targetSum,[])
        return Compelet_result
            