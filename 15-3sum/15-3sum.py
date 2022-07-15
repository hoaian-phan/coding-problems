class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # brute force
        
        results = []
        
        nums.sort()
        
        for left in range(len(nums) - 2):
            if nums[left] > 0:
                break
            elif left > 0 and nums[left] == nums[left - 1]:
                continue
            
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                sum_triplets = nums[left] + nums[mid] + nums[right] 
                if sum_triplets < 0:
                    mid += 1
                elif sum_triplets > 0:
                    right -= 1
                else:
                    results.append([nums[left], nums[mid], nums[right]])
                    mid += 1
                    while nums[mid] == nums[mid-1] and mid < right:
                        mid += 1
            
            
            
        return results
        