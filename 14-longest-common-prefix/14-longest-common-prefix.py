class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Approach: 
        # Sort the array by the length of strings using lambda function
        # Get the first word of the sorted array, also the shortest word in the string
        # Create common_prefix variable
        # Iterate through each char of the shortest word, 
            #then iterate through each word of the string, compare each letter
                # if the two letters are different, 
                    # return common prefix
            # add the new character to common_prefix
        # return the common prefix
        
        
        strs = sorted(strs, key=lambda word: len(word))
        
        shortest = strs[0]
        
        common_prefix = ""
        
        for i in range(len(shortest)):
            for j in range(len(strs)):
                if shortest[i] != strs[j][i]:
                    return common_prefix
                
            common_prefix += shortest[i]
        
        return common_prefix
                
        
                
            
        