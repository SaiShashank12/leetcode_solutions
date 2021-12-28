class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        longest = 1
        s = [(root, 1)]
        
        while s:
            u = s.pop()
            
            longest = max(longest, u[1])
            
            if u[0].left:
                if u[0].left.val - u[0].val == 1:
                    s.append((u[0].left, u[1] + 1))
                else:
                    s.append((u[0].left, 1))
            
            if u[0].right:
                if u[0].right.val - u[0].val == 1:
                    s.append((u[0].right, u[1] + 1))
                else:
                    s.append((u[0].right, 1))
                    
        return longest 