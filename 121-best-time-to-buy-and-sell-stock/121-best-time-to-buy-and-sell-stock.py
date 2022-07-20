class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
        # if prices have less than 2 items -> return 0
        # need to keep track of min price to buy
        # need to keep track of max profit so far
#         import math
#         if len(prices) < 2:
#             return 0
        
#         min_price = math.inf
#         max_profit = 0
        
#         for price in prices:
#             if price < min_price:
#                 min_price = price
#             else:
#                 profit = price - min_price
#                 max_profit = max(max_profit, profit)
                
#         return max_profit


        