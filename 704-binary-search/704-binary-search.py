class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # use binary search
        
        start = 0
        end = len(nums) - 1
        
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > target:
                end = mid - 1
            elif nums[mid] < target:
                start = mid + 1
            else:
                return mid
            
        return start if nums[start] == target else -1
            
            