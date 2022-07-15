class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        results = [1] * len(nums)
        
        prefix = 1
        for i in range(len(nums)):
            results[i] = prefix
            prefix *= nums[i]
            
        postfix = 1
        for j in range(len(nums)-1, -1, -1):
            results[j] *= postfix
            postfix *= nums[j]
            
        return results
                