class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # calculate left_sum and right_sum for index 0
        # while loops until the last index, calculate left_sum and right_sum
        # if same, return the index
        
        
        # i = 0
        left_sum = 0
        right_sum = sum(nums[1:])
        if left_sum == right_sum:
            return 0
        print(left_sum, right_sum)
        
        i = 1
        while i < len(nums):
            left_sum += nums[i-1]
            right_sum -= nums[i]
            if left_sum == right_sum:
                return i
            i += 1
            
        return -1
        
        