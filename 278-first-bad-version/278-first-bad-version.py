# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # use binary search algorithm
        
        start = 0
        end = n - 1
        
        while start < end:
            mid = (start + end) // 2
            if isBadVersion(mid):
                end = mid - 1
            else:
                start = mid + 1
        
        return start if isBadVersion(start) else start + 1
            