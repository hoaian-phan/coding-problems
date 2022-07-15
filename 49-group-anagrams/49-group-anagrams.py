class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # iterate through all the words in the list
        # make a dict {sorted string}: [list of words that have the same key]
        # return all the values of the dict
        
        anagram_dict = defaultdict(list)
        for word in strs:
            key = ''.join(sorted(word))
            print("key", key)
            anagram_dict[key].append(word)
            
        return anagram_dict.values()
                
                
        
        