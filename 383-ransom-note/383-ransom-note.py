class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # use one dictionary for magazine and iterate through ransomNote to check of existence
        
        magazine_dict = {}
        for char in magazine:
            magazine_dict[char] = magazine_dict.get(char, 0) + 1
            
        for letter in ransomNote:
            if letter not in magazine_dict:
                return False
            elif magazine_dict[letter] == 0:
                return False
            else:
                magazine_dict[letter] -= 1
                
        return True