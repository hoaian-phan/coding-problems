class Solution:
    def isPalindrome(self, s: str) -> bool:
        # use two pointers left and right 
        # while left < right, check if left and right is alphanumeric
        # if yes, compare them, if not same -> false
        # if not alphanumeric, increment left or decrement right accordingly
        # while loop stops, return True
        
        left = 0
        right = len(s) - 1
        
        while left < right:
            if s[left].isalnum() and s[right].isalnum():
                if s[left].lower() != s[right].lower():
                    print(left, s[left], right, s[right])
                    return False
                else: 
                    left += 1
                    right -= 1
            elif not s[left].isalnum():
                left += 1
            elif not s[right].isalnum():
                right -=1
            
                
        return True