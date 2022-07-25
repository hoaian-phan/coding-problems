# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iteratively, push all the left nodes onto the stack, then pop the last node, add to result, check the right, repeatedly
        
        results = []
        if not root: return results
        
        stack = []
        node = root
        while node or stack:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            results.append(node.val)
            node = node.right
                
        return results
                
        