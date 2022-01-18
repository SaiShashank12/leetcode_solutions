# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def plusOne(self, head: ListNode) -> ListNode:
        app=[]
        def get_int(head):
            while head:
                app.append(str(head.val))
                head=head.next
        def make_link(num):
            x=result=ListNode()
            
            for i in [int(a) for a in str(num)]:
                x.next=ListNode(i)
                x=x.next
            return result.next
        get_int(head)
        number=int("".join(app))+1
        
        
        return make_link(number)