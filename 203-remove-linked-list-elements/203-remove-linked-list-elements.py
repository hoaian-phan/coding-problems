# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        
        # if llist is empty
        if not head: return head
        
        # removing the only node
        if not head.next and head.val == val:
            return None
        
        # regular llist
        # if head node is the node to be removed
        while head and head.val == val:
            head = head.next
            
        # remove nodes other than head
        current = head
        while current and current.next:
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next
                
        return head