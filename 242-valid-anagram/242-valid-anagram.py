class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # use one dictionary for s, and iterate through t to check for existence
        if len(s) != len(t):
            return False
        
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
            
        for letter in t:
            if letter not in s_dict:
                return False
            elif s_dict[letter] == 0:
                return False
            else:
                s_dict[letter] -= 1
                
        return True
        
        