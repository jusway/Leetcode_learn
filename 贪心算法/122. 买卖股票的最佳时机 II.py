



class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        res=0
        for i in range(1,len(prices)): # 1,2,...,n-1
            if prices[i]>prices[i-1]:
                res+=prices[i] - prices[i - 1]

        return res
