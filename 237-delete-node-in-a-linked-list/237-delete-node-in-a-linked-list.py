# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        
        # change the value of the node to its next node
        # points to the next next node (skip next node)
        
        
        node.val = node.next.val
        node.next = node.next.next