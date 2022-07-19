# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if llist is empty -> return llist
        # use current and mid to keep track and traverse through the llist
        # current traverse at 2 times faster than mid
        
        if not head:
            return head
        
        current = head
        mid = current
        
        while current.next:
            if current.next.next:
                mid = mid.next
                current = current.next.next
            else:
                mid = mid.next
                current = current.next
                
        return mid