# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # use a set to keep track of visited nodes
        # traverse through the llist, check and add nodes to the set
        # return true if the node was seen before
        
        if not head or not head.next:
            return False
        
        seen = set()
        current = head
        seen.add(current)
        
        while current.next:
            if current.next in seen:
                return True
            else:
                seen.add(current.next)
                current = current.next
            
        return False