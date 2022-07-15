class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # make a dict {num: count}
        # sort dict by values
        # return slicing of dict.keys()[:k]
        
        num_dict = {}
        for num in nums:
            num_dict[num] = num_dict.get(num, 0) + 1
            
        sorted_num_dict = sorted(num_dict.items(), key=lambda x:x[1], reverse=True)
        
        sorted_dict = dict(sorted_num_dict)
        
        results = []
        for key in sorted_dict.keys():
            results.append(key)
            
        return results[:k]
            