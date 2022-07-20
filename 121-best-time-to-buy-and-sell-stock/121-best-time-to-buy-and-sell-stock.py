class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # if prices have less than 2 items -> return 0
        # need to keep track of min price to buy
        # need to keep track of max profit so far
        
        
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            if price < min_price:
                min_price = price
            else:
                profit = price - min_price
                max_profit = max(max_profit, profit)
                
        return max_profit


        