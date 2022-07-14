# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # head is null -> return null
        # use 2 pointers: i to traverse the linked list, j to keep track of middle node
        # j traverse behind i
        
        
        if not head:
            return None
        
        current = head
        mid = current
        
        while current:
            if current.next:
                if current.next.next:
                    mid = mid.next
                    current = current.next.next
                
                else:
                    mid = mid.next
                    current = current.next
                    
            else:
                print("inside", mid)
                return mid
        
        print("return", mid)        
        return mid
                
        