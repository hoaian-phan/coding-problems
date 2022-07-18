class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if list has fewer than 2 elements -> return 0
        # want to keep track of min price to buy and max profit
        # use 2 pointers to go through possible buy and sell prices
        
        if len(prices) < 2:
            return 0
        
        max_profit = 0
        
        i = 0
        j = 1
        while i < len(prices)-1 and j < len(prices):
            if prices[j] < prices[i]:
                i = j
                j += 1
            else:
                profit = prices[j] - prices[i]
                max_profit = max(max_profit, profit)
                j += 1
        
        return max_profit
        
        