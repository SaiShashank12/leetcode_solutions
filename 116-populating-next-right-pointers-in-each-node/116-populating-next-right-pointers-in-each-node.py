class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return
            
        level = deque([root])
        
        while level:
            nextLevel = deque()
            next = None
            
            while level:
                node = level.pop()
                
                if node.left:
                    nextLevel.appendleft(node.right)
                    nextLevel.appendleft(node.left)

                node.next, next = next, node
                
            level = nextLevel
                
        return root