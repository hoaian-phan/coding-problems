# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # use binary search algorithm to find first bad version
        
        start = 0
        end = n - 1
        
        while start < end:
            checking = (start + end) // 2
            if isBadVersion(checking):
                end = checking - 1
            elif not isBadVersion(checking):
                start = checking + 1
                
        if isBadVersion(start):
            return start
        elif not isBadVersion(start):
            return start + 1