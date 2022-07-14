class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        # create answers array
        # iterate from 0 to n, use conditionals to check for conditions
        
        answers = []
        
        for i in range(1, n+1):
            if i % 15 == 0:
                answers.append("FizzBuzz")
            elif i % 5 == 0:
                answers.append("Buzz")
            elif i % 3 == 0:
                answers.append("Fizz")
            else:
                answers.append(str(i))
                
        return answers
        
        