# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # if llist is empty or has only 1 node return None
        # use current pointer to traverse through the llist, keep track of visited nodes in a set data structure
        # if this node is already seen in the visited node set -> it's the start of the cycle
        
        if not head or not head.next:
            return None
        
        current = head
        visited_nodes = set()
        visited_nodes.add(head)
        
        while current.next:
            if current.next not in visited_nodes:
                visited_nodes.add(current.next)
                current = current.next
            else:
                return current.next
            
            
        return None
        