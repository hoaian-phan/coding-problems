# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # create a new list node and a current node to traverse and add results in
        # traverse through 2 input lists using two pointers, compare values and add to the result list
        # edge cases: both lists are empty and one list is empty
        
        if not list1 and not list2:
            return list1
        
        if not list1 or not list2:
            return list1 if not list2 else list2
        
        result = current = ListNode()
        
        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
            
        if list1:
            current.next = list1
        elif list2:
            current.next = list2
            
        return result.next
    
                