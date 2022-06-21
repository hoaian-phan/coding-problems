# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create a new head node of the result llist
        # Go through each node of the input lists, compare the two nodes, add the smaller data to the result node
        # If one list gets to the end, link the rest of the other list to the result llist
        
        result = ListNode()
        temp = result
        
        
        while list1 and list2:
            if list1.val <= list2.val:
                temp.next = list1
                temp = list1
                list1 = list1.next
                
            else:
                temp.next = list2
                temp = list2
                list2 = list2.next
                
        if not list1:
            temp.next = list2
        elif not list2:
            temp.next = list1
            
        return result.next
        
        
                
        
        
        