class Solution:
    def longestPalindrome(self, s: str) -> int:
        # use hashmap to keep track of the chars and their frequencies {char:frequency}
        # sum even frequencies and store in result
        # if there is an odd frequency, add it in result too
        
        maps = {}
        length = 0
        is_odd = False
        
        for char in s:
            maps[char] = maps.get(char, 0) + 1
            
        for value in maps.values():
            if value % 2 == 0:
                length += value
            elif value % 2 == 1:
                length += value - 1
                is_odd = True
                
        return length + 1 if is_odd else length