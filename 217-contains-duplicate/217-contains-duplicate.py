class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        # Edge cases:
        # empty list -> False
        # one element list -> False
        # Sort the list in ascending order so that the same values will be next to one another
        # Iterate through the list, compare the two adjacent values
        # If they are equal -> return True
        # If not, keep iterating
        # Done iteration, return False
        
        if len(nums) < 2:
            return False
        
        nums.sort()
        
        for index in range(len(nums) - 1):
            if nums[index] == nums[index + 1]:
                return True
            
        return False