class Solution:
    def firstUniqChar(self, s: str) -> int:
        # use Counter to count frequencies of each char, return the index of Counter == 1
        
        from collections import Counter
        
        counters = Counter(s)
        
        for index, char in enumerate(s):
            if counters[char] == 1:
                return index
            
        return -1