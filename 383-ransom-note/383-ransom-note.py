class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Make 2 dicts {char: count}
        # Compare keys: if magazine doesn't have key -> False
                        # else, if ransom[key] > magazine[key] -> False
        
        ransom_dict = {}
        magazine_dict = {}
        
        for char in ransomNote:
            ransom_dict[char] = ransom_dict.get(char, 0) + 1
            
        for letter in magazine:
            magazine_dict[letter] = magazine_dict.get(letter, 0) + 1
            
        print(ransom_dict)
        print(magazine_dict)
        for key in ransom_dict:
            if key not in magazine_dict:
                return False
            elif ransom_dict[key] > magazine_dict[key]:
                    return False
        return True