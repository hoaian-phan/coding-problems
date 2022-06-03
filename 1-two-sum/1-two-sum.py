class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute-force approach:
            # Using nested for loops to iterate through the indices of the array,
            # Check if the sum of two elements is the target
            # If yes, return the two indices
            # Runtime: O(n^2)
            # for i in range(len(nums) - 1):
            #     for j in range(i+1, len(nums)):
            #         if nums[i] + nums[j] == target:
            #             return [i,j]
                
        # Optimized approach:
            # Create a dictionary with keys being the numbers and values being the 
            # indices of the input list, initially empty
            # Iterate through input list using enumerate to access both index and num, calculate the difference of the target and check if it is in the num_dict
            # If not, add the num and its index as key:value pair to the dict
            # If yes, return the list of that index and the value at key difference in the dictionary
            # When the for loop ends but nothing return, meaning there are no two elements satisfy the requirement, return an empty list
            # Runtime: one for loop -> O(n)
            
            num_dict = {}
            for index, num in enumerate(nums):
                difference = target - num
                if difference not in num_dict:
                    num_dict[num] = index
                else:    
                    return [index, num_dict[difference]]
            
            return []
            
            
        
