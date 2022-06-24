# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Use 2 pointers fast and slow to keep track of traversing through the llist so that when the fast pointer traverse twice as fast as the the slow pointer. Then when the fast pointer reaches the end, the slow pointer is in the middle
        
        if not head:
            return 0
        
        fast = head
        slow = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        return slow
                
        
        