# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        rabbit=tortoise=head
        
        while rabbit and  rabbit.next:
            rabbit=rabbit.next.next
            tortoise=tortoise.next
            if rabbit==tortoise:
                rabbit=head
                while rabbit!=tortoise:
                    rabbit=rabbit.next
                    tortoise=tortoise.next
                return tortoise
        return None
            