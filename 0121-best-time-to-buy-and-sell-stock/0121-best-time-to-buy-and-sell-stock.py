from sys import maxsize

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        low = sys.maxsize
        maxd = 0
        
        if len(prices) == 1:
            return maxd
        
        for i in range(len(prices)):
            
            if prices[i] < low:
                low = prices[i]
            if maxd < prices[i] - low:
                maxd = prices[i] - low
            
        return maxd
