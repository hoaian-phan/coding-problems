# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # recursively
        levels = []
        
        if not root: return levels
        
        def bfs(node, level=0):
            if len(levels) == level:
                levels.append([])
                
            levels[level].append(node.val)
            
            if node.left:
                bfs(node.left, level + 1)
            if node.right:
                bfs(node.right, level + 1)
                
        bfs(root, 0)
        
        return levels
        
        
        
        
        
        
        # iteratively using queue
        
#         from collections import deque
        
#         levels = []
        
#         if not root: return levels
        
        
#         queue = deque([root])
        
#         while queue:
#             level = []
#             for n in range(len(queue)):
#                 node = queue.popleft()
#                 level.append(node.val)
#                 if node.left:
#                     queue.append(node.left)
#                 if node.right:
#                     queue.append(node.right)
#             levels.append(level)
        
#         return levels
#         