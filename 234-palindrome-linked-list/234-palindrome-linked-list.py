# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # traverse through the llist, add all values to a list
        # use algorithm to check for panlindrome of normal list
        
        if not head:
            return False
        
        lst = []
        current = head
        while current:
            lst.append(current.val)
            current = current.next
            
        print(lst)
        
        for i in range(len(lst) // 2):
            if lst[i] != lst[len(lst) - 1 - i]:
                return False
            
        return True