class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if arrays are sorted, use 2 pointers technique
        nums1.sort()
        nums2.sort()
        
        results = []
        
        i = 0
        j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                i += 1
            elif nums1[i] > nums2[j]:
                j += 1
            else:
                results.append(nums1[i])
                i += 1
                j += 1
                
        return results
                
        
        
        
        
        
        
        
        
        
        
        # brute force: make 2 dictionaries {num:count}
        # iterate through keys of dict_1 and check if they are in dict_2
        # if yes, add key to result list how many times depending on the min of the two values
        # O(n^2)
        
#         results = []
        
#         dict_1 = {}
#         for num in nums1:
#             dict_1[num] = dict_1.get(num, 0) + 1
            
#         dict_2 = {}
#         for num in nums2:
#             dict_2[num] = dict_2.get(num, 0) + 1
            
#         for key, value in dict_1.items():
#             if key in dict_2:
#                 min_value = min(value, dict_2[key])
#                 for n in range(min_value):
#                     results.append(key)
                    
#         return results
                