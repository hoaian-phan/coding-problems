class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert to string
        # check for palindrome as usual
        
        
        string = str(x)
        for i in range(len(string)//2):
            if string[i] != string[len(string)-1-i]:
                return False
            
        return True