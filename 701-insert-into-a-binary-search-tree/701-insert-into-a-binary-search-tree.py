# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        # traverse and compare current node value with value and find the place to insert 
        
        node = TreeNode(val)
        
        if not root: return node
        
        current = root
        previous = None
        while current:
            if current.val < val:
                previous = current
                current = current.right
            elif current.val > val:
                previous = current
                current = current.left
                
        if val < previous.val and not previous.left:
            previous.left = node
        elif val > previous.val and not previous.right:
            previous.right = node
            
        return root