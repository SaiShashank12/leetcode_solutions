# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        queue=collections.deque()
        queue.append(root)
        result=float("inf")
        ans=0
        while queue:
            tmp=queue.popleft()
            if result>abs(tmp.val-target):
                result=abs(tmp.val-target)
                ans=tmp.val
            
            
            if tmp.left:
                queue.append(tmp.left)
            if tmp.right:
                queue.append(tmp.right)
        return ans
            
             
            