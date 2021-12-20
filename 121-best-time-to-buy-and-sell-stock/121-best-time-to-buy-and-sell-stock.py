class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        
        if length == 1:
            return 0
        elif length == 2:
            if prices[0] >= prices[1]:
                return 0
            else:
                return prices[1] - prices[0]
        else:
            mini = prices[0]
            max_p = 0
            for i in range(1, length):
                if prices[i] < mini:
                    mini = prices[i]
                    
                elif mini < prices[i]:
                    profit = prices[i] - mini
                    if profit > max_p:
                        max_p = profit
                    
            return max_p