class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        minprice=prices[0]
        maxprofit=0
        for i in range(len(prices)):
            if prices[i]<minprice:
                minprice=prices[i]
            else:
                maxprofit=max(maxprofit,prices[i]-minprice)
        return maxprofit
        