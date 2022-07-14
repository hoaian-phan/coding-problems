class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # make a unique set of nums and compare the length of the set vs the list
        
        num_set = set(nums)
        
        return len(num_set) != len(nums)
        