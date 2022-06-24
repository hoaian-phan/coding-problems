# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # keep track of traversed node and its index in a dictionary
        # check each key to see if it is in the dict -> return value of it
        
        if not head or not head.next:
            return None
        
        current = head
        index = 0
        node_dicts = {}
        
        while current:
            if current not in node_dicts:
                node_dicts[current] = current
                index += 1
            else:
                return node_dicts[current]
            current = current.next
            
        return None