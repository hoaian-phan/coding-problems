class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # use sliding window technique
        
        if len(s) <= 1:
            return len(s)
        
        max_length = 0
        substring = {s[0]}
        
        i = 0
        j = 1
        
        while j < len(s):
            if s[j] not in substring:
                substring.add(s[j])
                j += 1
                max_length = max(max_length, len(substring))
            else:
                substring.remove(s[i])
                i +=1
                
        return max_length