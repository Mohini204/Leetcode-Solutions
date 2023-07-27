class Solution:
    
    def profitHelper(self, prices: List[int], s: int):
        
        if (s >= len(prices)):
            return 0
        
        maxp = 0
        
        for i in range(s,len(prices)):
            maxd = 0
            for j in range(i+1, len(prices)):
                if prices[i] < prices[j]:
                    profit = self.profitHelper(prices, j+1) + prices[j] - prices[i]
                    
                    if profit > maxd:
                        maxd = profit
            
            if maxd > maxp:
                maxp = maxd
                
        
        return maxp
    
    def maxProfit(self, prices: List[int]) -> int:
        
        total = 0
        
        for i in range(1,len(prices)):
            if prices[i] > prices[i-1]:
                total += prices[i] - prices[i-1]
                
            
        
        return total
    
    
        