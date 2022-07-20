class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # use one dictionary and map each char and word as key, index as value
        # compare to see if each pair has same value
        
        words = s.split()
        
        maps = {}
        
        if len(pattern) != len(words):
            return False
        
        for i in range(len(pattern)):
            char = pattern[i]
            word = words[i]
            
            word = "w_" + word
            
            if char not in maps:
                maps[char] = i
            if word not in maps:
                maps[word] = i
            if maps[char] != maps[word]:
                return False
            
        return True
            
            
        
        
        
        
        
        
        # split the s string by space to a list of words
        # use two pointers, make a dict {a:word}
        # compare char in pattern with value of the same key in dict
        
#         words = s.split()
#         print(words)
        
#         if len(pattern) != len(words):
#             return False
        
#         pattern_dict = {}
        
#         for char, word in zip(pattern, words):
#             if char not in pattern_dict:
#                 if word in pattern_dict.values():
#                     return False
#                 pattern_dict[char] = word
#             elif word != pattern_dict[char]:
#                 return False
            
#         return True
            
        