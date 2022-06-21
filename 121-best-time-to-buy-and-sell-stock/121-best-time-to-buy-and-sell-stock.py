class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        import math
        if len(prices) < 2:
            return 0

        max_profit = 0
        min_price = math.inf
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                max_profit = max(max_profit, price - min_price)

        return max_profit
        
        
        
        