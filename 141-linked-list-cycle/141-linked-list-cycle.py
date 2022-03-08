# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        rabbit=head.next
        tortoise=head
        
        
        while rabbit!=tortoise:
            if not rabbit or not rabbit.next:
                return False
            rabbit=rabbit.next.next
            tortoise=tortoise.next
            
        return True