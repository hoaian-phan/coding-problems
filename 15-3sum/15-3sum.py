class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # sort the list to avoid duplicate
        # looping through the list forr the left number
        # use two pointers for mid and right index similarly as in two sum problem
        
        
        nums.sort()
        
        results = []
        
        for left in range(len(nums) - 2):
            # if the first number is positive, can't find the other 2 positive nums that sum up to 0
            if nums[left] > 0:
                break
            # avoid duplicate for first num
            elif left > 0 and nums[left] == nums[left-1]:
                continue
            
            # use two pointers as in two sum
            mid = left + 1
            right = len(nums) - 1
            while mid < right:
                three_sum = nums[left] + nums[mid] + nums[right]
                if three_sum < 0:
                    mid += 1
                elif three_sum > 0: 
                    right -= 1
                else:
                    results.append([nums[left],nums[mid],nums[right]])
                    # keep looking for more values of 2nd and 3rd num
                    mid += 1
                    # avoid duplicate for 2nd num
                    while nums[mid] == nums[mid-1] and mid < right:
                        mid += 1
        
        return results
            