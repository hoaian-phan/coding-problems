class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        # while loops until the last index, calculate left_sum and right_sum
        # if same, return the index
        
        
        i = 0
        while i < len(nums):
            left_sum = sum(nums[:i])
            right_sum = sum(nums[i+1:])
            
            if left_sum == right_sum:
                return i
            i += 1
            
        return -1
        
        