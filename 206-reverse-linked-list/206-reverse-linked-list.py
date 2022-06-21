# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Create a prev points to null
        # Traverse through the llist while head is not empty
            # next_node points to head.next
            # head.next points to prev
            # prev is head
            # head is next_node
        # Return prev
        
        
        prev = None
        next_node = ListNode()
        
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
            
        return prev
            
        