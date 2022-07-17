class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # create dictionaries {char:[indices]}
        # compares values of 2 dictionaries
        
        s_dict = defaultdict(list)
        for index, char in enumerate(s):
            s_dict[char].append(index)
        
        t_dict = defaultdict(list)
        for index, char in enumerate(t):
            t_dict[char].append(index)
        
        for value in s_dict.values():
            if value not in t_dict.values():
                return False
            
        return True