# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        # have a variable to keep track of the min distance and closest value
        # traverse down the BST to find the value, 
        # at every level, update the closest value
        # if can't find it, return the closest value
        import math
        min_diff = math.inf
        closest = math.inf
        
        
        current = root
        while current:
            if target == current.val:
                return current.val
            if abs(current.val - target) < min_diff:
                min_diff =  abs(current.val - target)
                closest = current.val
            if target < current.val:
                current = current.left
            elif target > current.val:
                current = current.right
                
        return closest
        