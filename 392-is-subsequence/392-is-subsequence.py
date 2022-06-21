class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # if s is empty -> True
        # if length of s > length of t -> False
        # use 2 pointers to check the two strings
        
        if len(s) == 0:
            return True
        
        if len(s) > len(t):
            return False
        
        s_pointer = 0
        t_pointer = 0
        
        while t_pointer < len(t):
            if t[t_pointer] == s[s_pointer]:
                s_pointer += 1
                if s_pointer == len(s):
                    return True
            t_pointer += 1
            
        return False
            
            
                    
            