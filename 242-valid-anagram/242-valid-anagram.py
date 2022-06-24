class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Make 2 dictionaries {char: count}
        # Return dict_1 == dict_2
        
        dict_s = {}
        dict_t = {}
        
        for char in s:
            dict_s[char] = dict_s.get(char, 0) + 1
            
        for letter in t:
            dict_t[letter] = dict_t.get(letter, 0) + 1
            
        return dict_s == dict_t