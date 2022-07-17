class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # create max_sum and current sum
        # iterate through nums list, checking if num is larger than current_sum, if yes, update current_sum
        # if not, add it to the current sum
        # and calculate max_sum by comparing current sum and max_sum
        # runtime: O(n)
        
        
        import math
        max_sum = -math.inf
        current_sum = -math.inf
        
        for num in nums:
            if current_sum + num < num:
                current_sum = num
                
            else:
                current_sum += num
                
            max_sum = max(max_sum, current_sum)
            
                
        return max_sum