# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # use 3 pointers: current, previous, next to keep track and reverse the llist
        
        if not head:
            return head
        
        
        previous = None
        current = head
        next_pt = None
        
        while current:
            next_pt = current.next
            current.next = previous
            previous = current
            current = next_pt
            
        return previous