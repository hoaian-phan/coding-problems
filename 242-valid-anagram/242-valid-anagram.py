class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # make 2 dicts {char:count}
        # compare the two dicts: if equal -> True, else False
        
        s_dict = {}
        for char in s:
            s_dict[char] = s_dict.get(char, 0) + 1
            
        t_dict = {}
        for letter in t:
            t_dict[letter] = t_dict.get(letter, 0) + 1
            
        return s_dict == t_dict