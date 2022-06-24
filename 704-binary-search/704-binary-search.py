class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        # Choose a number which is in the middle of the list and compare to target
        # Adjust the range and recalculate mid num and so on
        
        
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] < target:
                start = mid + 1
            elif nums[mid] > target:
                end = mid - 1
            else:
                return mid
            
        return -1
        