class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # use two pointers to compare each char
        # if not the same, move t_pointer up to search the whole string (until a certain index)
        # if same, move both pointer up 
        
        i = 0
        j = 0
        
        while i < len(s) and j < len(t) - len(s) + i + 1:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
                
        return True if i >= len(s) else False
            