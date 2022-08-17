# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        def list_link(head):
            result=[]
            while(head):
                result.append(head.val)
                head=head.next
            return result
        def link_list(result):
            head1=ListNode()
            tmp=head1
            for i in result:
                tmp.next=ListNode(i)
                tmp=tmp.next
            return head1.next
        result=list_link(head)
        result.reverse()
        return link_list(result)
            
        