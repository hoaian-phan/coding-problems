class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        # Approach:
        # Make a list of three sets, each set contains all the letters on each row of the keyboard
        # Create a result list
        # Iterate through the keyboard set list
            # Iterate through each word in the input list
                # Convert each word to a set of characters 
                # Check if the set is a subset of the keyboard sets
                    # if yes -> add to the result list
        # Return result list
        
        keyboard_set_list = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        
        result_list = []
        for keyboard_set in keyboard_set_list:
            for word in words:
                word_set = set(word.lower())
                if word_set.issubset(keyboard_set):
                    result_list.append(word)
                    
        return result_list
            
        