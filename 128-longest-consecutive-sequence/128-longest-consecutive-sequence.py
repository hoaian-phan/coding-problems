class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # sort the list
        # create longest = 0
        # create count to keep track
        # iterate through the sorted list, compare two elements
        # if difference is 1 -> increment count, calculate longest = max(count, longest)
        
        if len(nums) < 2:
            return len(nums)
        
        nums.sort()
        longest = 0
        count = 1
        
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                continue
            elif nums[i+1] - nums[i] == 1:
                count += 1
                longest = max(count, longest)
            else:
                count = 1
                
        return max(longest, count)