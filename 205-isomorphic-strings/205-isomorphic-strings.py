class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        # if length of s and t are not the same -> false
        # Make 2 dicts {char:(index,index,index)}
        # Compare the values of the two dicts
            # same -> True
            # not -> False
            
        if len(s) != len(t):
            return False
        
        if s == t:
            return True
        
        dict1 = {s[0]:[0]}
        dict2 = {t[0]:[0]}
        
#         for char in s:
#             dict1[char] = dict1.get(char, 0) + 1
            
#         for char in t:
#             dict2[char] = dict2.get(char, 0) + 1
            
        for i in range(1, len(s)):
            # if s[i] == t[i]:
            #     return False
            if s[i] not in dict1:
                dict1[s[i]] = [i]
            else:
                dict1[s[i]].append(i)
            if t[i] not in dict2:
                dict2[t[i]] = [i]
            else:
                dict2[t[i]].append(i)
            
            
        print(dict1)
        print(dict2)
        
        for value in dict1.values():
            if value not in dict2.values():
                return False
                
        return True