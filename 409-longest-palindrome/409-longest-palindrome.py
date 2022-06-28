class Solution:
    def longestPalindrome(self, s: str) -> int:
        # Create a dict {char:count} for the input string
        # longest_palindrome = add all even values
                    # then plus all odd values - 1
                    # if there is a value = 1 -> plus 1
                
        character_count = {}
        for char in s:
            character_count[char] = character_count.get(char, 0) + 1
            
        print(character_count)
        
        longest_palindrome_length = 0
        
        for value in character_count.values():
            print(value, longest_palindrome_length)
            if value % 2 == 0:
                longest_palindrome_length += value
            elif value % 2 == 1:
                longest_palindrome_length += (value - 1)
        
        if longest_palindrome_length < len(s):
            return longest_palindrome_length + 1
        
        return longest_palindrome_length