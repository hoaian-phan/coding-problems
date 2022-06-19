class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # At index 0, calculate right and left sum and compare
        # Iterate through index 1 to end, calculate right and left by subtracting and adding element at index and compare the sum
        # If the two sums are equal -> return the index
        
        
        right_sum = sum(nums[1:])
        left_sum = 0
        
        if right_sum == left_sum:
            return 0
        
        for i in range(1,len(nums)):
            left_sum += nums[i-1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
        
        return -1