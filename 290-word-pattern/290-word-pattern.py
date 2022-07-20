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
        value_set = set()
        
        for i in range(len(pattern)):
            print(pattern_dict)
            if pattern[i] not in pattern_dict and words[i] not in value_set:
                pattern_dict[pattern[i]] = words[i]
                value_set.add(words[i])
            elif pattern[i] not in pattern_dict and words[i] in value_set:
                return False
            elif pattern[i] in pattern_dict and words[i] != pattern_dict[pattern[i]]:
                print(pattern[i], pattern_dict[pattern[i]] )
                return False
    
            
        return True
            
        