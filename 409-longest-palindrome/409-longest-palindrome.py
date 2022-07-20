class Solution:
    def longestPalindrome(self, s: str) -> int:
        # use hashmap to keep track of the chars and their frequencies {char:frequency}
        # sum even frequencies and store in result
        # if there is an odd frequency, add it in result too
        
        maps = {}
        length = 0
        
        for char in s:
            maps[char] = maps.get(char, 0) + 1
            
        for value in maps.values():
            length += value // 2 * 2
            if value % 2 == 1 and length % 2 == 0:
                length += 1
                
        return length 