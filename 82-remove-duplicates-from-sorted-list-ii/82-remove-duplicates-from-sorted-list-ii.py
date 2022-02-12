# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr=head
        new_head=prev=ListNode(next=head)
        while curr:
            present=curr.val
            if curr.next and present==curr.next.val:
                while curr.next and present==curr.next.val:
                    curr=curr.next
                prev.next=curr.next
                curr=curr.next
                continue
            prev=curr
            curr=curr.next
        return new_head.next
                