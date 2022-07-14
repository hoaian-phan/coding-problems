class Solution:
    def romanToInt(self, s: str) -> int:
        # create a result variable
        # make a dict {roman:numeral} including all special cases
        # iterate through the string
            # check if IX -> add dict[IX]
            # if IV -> add dict[IV]
            # ...
            # else, add dict[element]
            
            
        result = 0
        
        roman_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        
        i = 0
        while i < len(s) - 1:
            if s[i] == "I" and s[i+1] in ["V", "X"] or s[i] == "X" and s[i+1] in ["L", "C"]  or s[i] == "C" and s[i+1] in ["D", "M"]:
                result += roman_dict[s[i]+s[i+1]] 
                i += 2
            else:
                result += roman_dict[s[i]]
                i += 1
                
        return result if i >= len(s) else result + roman_dict[s[i]]
        
        