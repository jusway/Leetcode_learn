from functools import cache


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        @cache
        def f(i,holding): # 0~i天 结束时持有状态为 holding 的最大利润
            if i==0:
                return -prices[0] if holding else 0

            # 第 i 天结束时候持有股票
            if holding:
                # i-1 天结束时没有股票，但是今天购入
                a =f(i-1,0)-prices[i]
                # i-1 天结束时持有股票，同时今天什么也不做
                b=f(i-1,1)
                return max(a,b)
            else:  # 第 i 天结束时没有股票
                # i-1 天结束时有股票，但是今天卖了
                a=f(i-1,1)+prices[i]
                # i-1 天结束时没有股票，同时今天什么也不做
                b=f(i-1,0)
                return max(a,b)

        return f(n-1,0)

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp= [[0]*2 for _ in range(n)]
        dp[0][1]=-prices[0]
        for i in range(1,n): # 1,2,...,n-1
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        return dp[n-1][0]


# 滚动变量
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        free, hold = 0, -prices[0]  # 第 0 天结束时的两个状态
        for i in range(1, len(prices)):
            free, hold =max(free, hold + prices[i]), max(hold, free - prices[i])

        return free



