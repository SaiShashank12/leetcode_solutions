# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def __init__(self):
        self.root=None
    def link(self,i):
        if not self.root:
            self.root=ListNode(i)
            return 
        curr=self.root
        while curr.next:
            curr=curr.next
        curr.next=ListNode(i)
    def inserted(self,arr):
        for i in range(1, len(arr)):

            key = arr[i]

            # Move elements of arr[0..i-1], that are
            # greater than key, to one position ahead
            # of their current position
            j = i-1
            while j >= 0 and key < arr[j] :
                    arr[j + 1] = arr[j]
                    j -= 1
            arr[j + 1] = key
        return arr
        
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        gg=[]
        head1=head
        while head1:
            if not head1:
                break
            gg.append(head1.val)
            head1=head1.next
        self.inserted(gg)
        for i in gg:
            self.link(i)
        return self.root