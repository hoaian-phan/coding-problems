"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # iteratively:
        from collections import deque
        
        if not root: return
        
        results = []
        queue = deque([root])
        
        while queue:
            node = queue.popleft()
            results.append(node.val)

            for child in reversed(node.children):
                queue.appendleft(child)
            
        return results
        
        
        
        # using depth first search algorithm, recursively
        
#         results = []
        
#         def dfs(node):
#             if not node: return
            
#             results.append(node.val)
#             for child in node.children:
#                 dfs(child)
        
#         dfs(root)
        
#         return results
        