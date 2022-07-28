# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # traverse and compare current node value with input value
        # if greater -> move left, if less -> move right, if equal -> return current node
        if not root: return root
        
        current = root
        while current:
            if current.val == val:
                return current
            elif current.val > val:
                current = current.left
            else:
                current = current.right
                
        return None