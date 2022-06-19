class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Iterate through half of the string, swap the first and last element
        
        for i in range(len(s) // 2):
            s[i], s[-i-1] = s[-i-1], s[i]
            
        
        