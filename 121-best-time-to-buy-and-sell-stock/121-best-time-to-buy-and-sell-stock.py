class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create a max_profit to keep track of max profit
        # use two pointers left (buy) and right (sell)
        # if element at left > element at right -> update left = right because we want to buy at lower price
        # move right along the list and calculate profit, compare and update max profit
        # return max_profit
        
        max_profit = 0
        
        left = 0
        right = 1
        while right < len(prices):
            if prices[right] > prices[left]:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
                
            right += 1
                
        return max_profit
        