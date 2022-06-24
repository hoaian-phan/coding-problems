# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # keep track of traversed node in a set
        # check each key to see if it is in the set -> return value of it
        
        if not head or not head.next:
            return None
        
        current = head
        node_set = set()
        
        while current:
            if current not in node_set:
                node_set.add(current)
            else:
                return current
            current = current.next
            
        return None