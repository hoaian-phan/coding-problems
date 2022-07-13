class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        # calculate each person's wealth by using sum function
        # keep track of max_wealth and update accordingly by comparing each person's wealth vs max_wealth
        
        max_wealth = 0
        
        for person in accounts:
            wealth = sum(person)
            max_wealth = max([max_wealth, wealth])
            
        return max_wealth