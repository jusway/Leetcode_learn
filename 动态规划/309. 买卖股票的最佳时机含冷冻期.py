from functools import cache


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        @cache
        def f(i,state): # 0~i天中 结束时状态为state 最大利润
            # state： 0 “没有股票” 1 “持有股票” 2 “冷冻期”
            if i ==0:
                if state==0:
                    return 0
                elif state==1:
                    return -prices[0]
                elif state==2:
                    return float("-inf")


            if state == 0:
                # 前一天没有股票，然后休息 ; 前一天是冷冻期，然后休息
                return max(f(i-1,0),f(i-1,2))
            elif state == 1:
                # 前一天没有股票，然后买入 ; 前一天持有股票，然后休息
                return max(f(i-1,0)-prices[i],f(i-1,1))
            elif state == 2:
                # 前一天持有股票，然后卖了
                return f(i-1,1)+prices[i]

        return max( f(n-1,0),f(n-1,2))


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        n=len(prices)
        dp= [[0]*3 for _ in range(n)]
        dp[0][1]=-prices[0]
        dp[0][2]=float("-inf")
        for i in range(1,n): # 1,2,...,n-1
            dp[i][0]= max(dp[i-1][0],dp[i-1][2])
            dp[i][1]= max(dp[i-1][0]-prices[i],dp[i-1][1])
            dp[i][2]= dp[i-1][1]+prices[i]

        return max(dp[n-1][2], dp[n-1][0])



