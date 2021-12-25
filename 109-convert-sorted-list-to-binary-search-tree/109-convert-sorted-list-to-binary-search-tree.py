# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def half(head):
            if not head:
                return head
            end=mid=head
            prev=None
            while end and end.next:
                end=end.next.next
                prev=mid
                mid=mid.next
                
            return prev,mid
        def helper(head):
            if not head:
                return None
            prev,mid=half(head)
            if prev:
                prev.next=None
            root=TreeNode(mid.val)
            if head==mid:
                return root
            
            
            root.left=helper(head)
            root.right=helper(mid.next)
            return root
                
            
        #print(half(head)[0].val)
        return helper(head)