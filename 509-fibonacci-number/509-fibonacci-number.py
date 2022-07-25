class Solution:
    def fib(self, n: int) -> int:
        
        memo = {}
        
        if n in memo: return memo[n]
        
        for i in range(n+1):
            if i == 0:
                memo[i] = 0
            elif i == 1:
                memo[i] = 1
            else:
                memo[i] = memo[i-1] + memo[i-2]
                
        return memo[n]
        