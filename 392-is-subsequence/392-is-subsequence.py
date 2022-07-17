class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # use two pointers to compare each char
        # if not the same, move t_pointer up to search the whole string (until a certain index)
        # if same, move both pointer up 
        
        if len(s) == 0:
            return True
        
        if len(s) > len(t):
            return False
    
        
        i = 0
        j = 0
        
        while i < len(s) and j < len(t) - len(s) + i + 1:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                j += 1
                
        return i == len(s)
            