class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # use two pointers left (start index) and right (end index)
        # check the sum of 2 elements at left and right, compare with target
        # if sum < target, move left index forward
        # if sum > target, move right index forward
        # else sum == target, return left + 1 and right + 1
        
        left = 0 
        right = len(numbers) - 1
        
        while left < right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else: 
                return [left+1, right+1]
        