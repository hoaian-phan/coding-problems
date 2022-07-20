class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        # split the s string by space to a list of words
        # use two pointers, make a dict {a:word}
        # compare char in pattern with value of the same key in dict
        
        words = s.split()
        print(words)
        
        if len(pattern) != len(words):
            return False
        
        pattern_dict = {}
        
        for char, word in zip(pattern, words):
            if char not in pattern_dict:
                if word in pattern_dict.values():
                    return False
                pattern_dict[char] = word
            elif word != pattern_dict[char]:
                return False
            
        return True
            
        