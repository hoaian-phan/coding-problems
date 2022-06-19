class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # Iterate through each index, calculate the sum of left vs right by using slicing and sum()
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