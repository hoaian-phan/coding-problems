class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert the number to string
        # Iterate through the string to the middle
        # compare the first and last char
        # if not the same -> not palindrome
        # end of loops, return True
        
        x_string = str(x)
        print(x_string)
        
        i = 0
        while i < len(x_string) // 2:
            if x_string[i] != x_string[len(x_string) - 1 - i]:
                return False
            i += 1
            
        return True
        