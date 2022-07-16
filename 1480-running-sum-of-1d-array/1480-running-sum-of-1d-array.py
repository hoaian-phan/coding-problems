class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # iterate through the list and add current element to sum
        # add new sum to result list
        
        running_sum = []
        current_sum = 0
        for num in nums:
            current_sum += num
            running_sum.append(current_sum)
            
        return running_sum