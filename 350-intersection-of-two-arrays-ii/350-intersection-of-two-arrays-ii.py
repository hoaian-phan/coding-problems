class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # if arrays are sorted, use 2 pointers technique
        # runtime: O(n log n + m log m)
#         nums1.sort()
#         nums2.sort()
        
#         results = []
        
#         i = 0
#         j = 0
        
#         while i < len(nums1) and j < len(nums2):
#             if nums1[i] < nums2[j]:
#                 i += 1
#             elif nums1[i] > nums2[j]:
#                 j += 1
#             else:
#                 results.append(nums1[i])
#                 i += 1
#                 j += 1
                
#         return results
                
        
        
        
        
        
        
        
        
        
        
        # brute force: make 1 dictionary {num:count}
        # iterate through the other list, check if element is in dictionary
        # if yes, add key to result list how many times depending on the min of the two values
        # O(n * m)
        
        results = []
        
        dict_1 = {}
        for num in nums1:
            dict_1[num] = dict_1.get(num, 0) + 1
            
        for num in nums2:
            if num in dict_1 and dict_1[num] > 0:
                results.append(num)
                dict_1[num] -= 1
                print(dict_1[num])
        print(dict_1)
                
            
                    
        return results
                