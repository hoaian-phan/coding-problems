class Solution:
    def numberOfSteps(self, num: int) -> int:
        # keep counter
        # while num is larger than 0, do the following:
         # if num is even, divide by 2, increment counter
         # else, subtract 1 from num, increment counter
        
        
        counter = 0
        
        while num > 0:
            if num % 2 == 0:
                num = num / 2
            else:
                num = num - 1
            counter += 1
            
        return counter
                