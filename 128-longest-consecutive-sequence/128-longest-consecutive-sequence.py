class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # using set to search for element -> O(n)
        # keep longest variable
        # go through each num and check to see
        # if it is the start of a sequence (no left value in the set) -> start count
            # while its right value in the set -> increment count, increment num
            # update longest by comparing longest and count
            
        num_set = set(nums)
        longest = 0
        count = 0
        
        for num in nums:
            if num -1 not in num_set:
                count = 1
                while num + count in num_set:
                    count += 1
                    
                longest = max(longest, count)
            
        return longest
        
        
        
        
        
        # Brute force: sort the list
        # create longest = 0
        # create count to keep track
        # iterate through the sorted list, compare two elements
        # if difference is 1 -> increment count, calculate longest = max(count, longest)
        #runtime: O (n log n)
        
#         if len(nums) < 2:
#             return len(nums)
        
#         nums.sort()
#         longest = 0
#         count = 1
        
#         for i in range(len(nums)-1):
#             if nums[i+1] == nums[i]:
#                 continue
#             elif nums[i+1] - nums[i] == 1:
#                 count += 1
#                 longest = max(count, longest)
#             else:
#                 count = 1
                
#         return max(longest, count)