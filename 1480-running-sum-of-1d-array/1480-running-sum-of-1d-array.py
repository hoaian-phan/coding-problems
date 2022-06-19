class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        # iterate through each number in the list, add num to current sum, add sum to result list
        
        running_sums = []
        
        sum = 0
        for num in nums:
            sum += num
            running_sums.append(sum)
            
        return running_sums