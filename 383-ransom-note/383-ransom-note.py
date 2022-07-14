class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # make two dicts {char:count}
        # each key in ransom has to present in magazine, with value <= value in magazine -> True
        
        ransom = {}
        for char in ransomNote:
            ransom[char] = ransom.get(char, 0) + 1
        print("ransom", ransom)
            
        magazines = {}
        for letter in magazine:
            magazines[letter] = magazines.get(letter, 0) + 1
        print("magazines", magazines)
            
        for key, value in ransom.items():
            print(key)
            if key not in magazines:
                return False
            elif value > magazines[key]:
                return False
            
        return True