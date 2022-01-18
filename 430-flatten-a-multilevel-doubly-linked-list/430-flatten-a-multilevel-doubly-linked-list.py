"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        
        def make_flat(head):
            nonlocal x
            if head:
                if x.val:
                    prev=x
                else:
                    prev=None
                x.next=Node(head.val)
                x.next.prev=prev
                x=x.next
            if head.child:
                make_flat(head.child)
            if head.next:
                make_flat(head.next)
        result=x=Node()
        if not head:
            return head
        make_flat(head)
        return result.next