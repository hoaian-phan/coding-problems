class Solution:
    def isPalindrome(self, x: int) -> bool:
        # without converting to str, reverse half of the input number
        if x == 0:
            return True
        
        if x < 0 or x % 10 == 0:
            return False
        
        h_reverse = 0
        
        while x > h_reverse:
            remainder = x % 10
            h_reverse = h_reverse * 10 + remainder
            x = x // 10
            
        
        return True if (h_reverse // 10 == x) or (h_reverse == x) else False
        
        
        
        
        
        
        
        
        
        
        # without converting to str, reverse the whole input number
        
#         if x == 0:
#             return True
        
#         if x < 0 or x % 10 == 0:
#             return False
        
        
#         reverse = 0
#         temp = x
        
#         while temp > 0:
#             remainder = temp % 10
#             reverse = reverse * 10 + remainder
#             temp = temp // 10
#         print(x, reverse)
            
#         return x == reverse
        
        
        # convert to string
        # check for palindrome as usual
        
#         if x < 0: return False
        
#         string = str(x)
#         for i in range(len(string)//2):
#             if string[i] != string[len(string)-1-i]:
#                 return False
            
#         return True