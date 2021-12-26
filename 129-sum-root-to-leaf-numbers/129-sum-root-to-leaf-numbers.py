# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def helper(root,result):
            nonlocal sum1
            if not root:
                return 
            result.append(root.val)
            if root.left:
                helper(root.left,result)
            if root.right:
                helper(root.right,result)
            if not root.left and not root.right:
                num=0
                #result=result[::-1]
                k=len(result)-1
                for i in range(len(result)):
                    num+=result[i]*(10**k)
                    k-=1
                sum1+=num
            result.pop()
        sum1=0
        helper(root,[])
        return sum1