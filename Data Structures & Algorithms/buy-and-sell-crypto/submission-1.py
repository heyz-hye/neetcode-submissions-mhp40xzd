class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price=prices[0]
        max_profit=0

        if len(prices)<2:
            return max_profit
        
        for i in range(len(prices)):
            if prices[i]<min_price:
                min_price=prices[i]

            else:
                total=prices[i]-min_price
                max_profit=max(max_profit,total)

        return max_profit
        
        