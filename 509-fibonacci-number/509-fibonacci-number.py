class Solution:
    def fib(self, n: int) -> int:
        # Use cache 
        
        cache = {}
        if n in cache:
            return cache[n]
        
        if n < 2:
            return n
        
        cache[n] = self.fib(n-1) + self.fib(n-2)
        
        return cache[n]
        
        