class Solution:
    def romanToInt(self, s: str) -> int:
        # Make a dictionary to store roman letter: integer as key: value
        # Create a num integer = 0
        # Iterate through the input string s, checking each char
            # If char is I and not at end of string, check next char
                # If next char is V -> add 5 to num
                # If next char is X -> add 9 to num
            # If char is X and not at end of string, check next char
                # If next char is L -> add 50 to num
                # If next char is C -> add 90 to num
            # If char is C and not at end of string, check next char
                # If next char is D -> add 500 to num
                # If next char is M -> add 900 to num
        # Return num
        
        roman_int = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        
        num = 0
        
        i = 0
        while i < len(s):
            if i < len(s) - 1 and s[i] == "I":
                if s[i+1] == "V":
                    num += 4
                    i += 1
                elif s[i+1] == "X":
                    num += 9
                    i += 1
                else:
                    num += 1
                
            elif i < len(s) - 1 and s[i] == "X":
                if s[i+1] == "L":
                    num += 40
                    i += 1
                elif s[i+1] == "C":
                    num += 90
                    i += 1
                else:
                    num += 10
            elif i < len(s) - 1 and s[i] == "C":
                if s[i+1] == "D":
                    num += 400
                    i += 1
                elif s[i+1] == "M":
                    num += 900
                    i += 1
                else:
                    num += 100
            else:
                num += roman_int[s[i]]
            i += 1
                
        return num