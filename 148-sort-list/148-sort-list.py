class Solution:
    def tolist(self,head):
        thelist=[]
        while head:
            thelist.append(head.val)
            head=head.next
        return thelist
    def make_link(self,array,new_head):
        
        for i in range(len(array)):
            new_head.val=array[i]
            if i>=len(array)-1:
                break
            new_head.next=ListNode()
            new_head=new_head.next
        
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        thelist=self.tolist(head)
        thelist.sort()
        new_head=ListNode()
        self.make_link(thelist,new_head)
        return new_head