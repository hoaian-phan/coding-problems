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
        
        for num in nums:
            if (num-1) not in num_set:
                count = 1
                while (num + count) in num_set:
                    count += 1
                    
                longest = max(longest, count)
            
        return longest
      