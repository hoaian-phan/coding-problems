class Solution:
    def fib(self, n: int) -> int:
        # Use cache 
        
        cache = {0: 0, 1: 1}
        
        for n in range(2, n+1):
            cache[n] = cache[n-1] + cache[n-2]
        
        return cache[n]
        
        