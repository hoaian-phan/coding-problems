class Solution:
    def fib(self, n: int) -> int:
        # Use recursion
        # base case 0 and 1
        # recursive case sum of fib(n-1) + fib(n-2)
        
        if n == 0: return 0
        elif n == 1: return 1
        
        return self.fib(n-1) + self.fib(n-2)