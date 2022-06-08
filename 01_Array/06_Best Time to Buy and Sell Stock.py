class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minStockPrice = float('inf')
        maxProfit = 0
        
        for elem in prices:
            if elem < minStockPrice:
                minStockPrice = elem
            if elem - minStockPrice > maxProfit:
                maxProfit = elem - minStockPrice
        
        return maxProfit