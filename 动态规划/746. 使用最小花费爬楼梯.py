from functools import cache


# 朴素递归+记忆化搜索
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:

        @cache
        def f(i): # 0 走到 i 台阶的 最低花费
            if i==0:
                return 0
            if i==1:
                return 0

            # 上一步走了一步
            one=f(i-1)+cost[i-1]
            # 上一步走了两步
            two=f(i-2)+cost[i-2]
            return min(one,two)

        return f(len(cost))

# 动态规划
class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n=len(cost)
        dp=[0]*(n+1)
        for i in range(2,n+1): # 2,3,...,n-1,n
            dp[i]=min(dp[i-1]+cost[i-1],dp[i-2]+cost[i-2])

        return dp[n]








