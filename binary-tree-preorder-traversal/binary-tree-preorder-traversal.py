# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # iteratively
        from collections import deque
        
        results = []
        
        if not root: return results
        
        possible_nodes = deque([root])
        while possible_nodes:
            node = possible_nodes.popleft()
            results.append(node.val)
            if node.right:
                possible_nodes.appendleft(node.right)
            if node.left:
                possible_nodes.appendleft(node.left)
            
                
        return results
            
        
        
        