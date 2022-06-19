class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Iterate through each number by index
            # if sum + num < num -> reset sum to num
            # else: add num to sum
            
            # update largest num along the way
        
        largest_sum = nums[0]
        sum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > sum + nums[i]:
                sum = nums[i]
            else:
                sum += nums[i]
            
            if sum >largest_sum:
                largest_sum = sum
                
        return largest_sum
                
        
                