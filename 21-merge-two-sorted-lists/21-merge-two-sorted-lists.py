# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(head,l):
            if not head:
                return 
            l.append(head.val)
            helper(head.next,l)
        def make_list(l):
            res=head=ListNode()
            for i in l:
                head.next=ListNode(i)
                head=head.next
            return res.next
        l1=[]
        l2=[]
        helper(list1,l1)
        helper(list2,l2)
        return make_list(sorted(l1+l2))
                
            