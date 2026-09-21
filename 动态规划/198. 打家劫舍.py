from functools import cache
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        max_money=-float("inf")

        def backtracking(i,cur_money): # 当前i位置偷还是不偷？
            nonlocal max_money
            if i>=n:
                max_money=max(cur_money,max_money)
                return

            # 偷
            cur_money+=nums[i]
            backtracking(i+2,cur_money)
            # 回溯
            cur_money-=nums[i]
            # 不偷
            backtracking(i+1,cur_money)

        backtracking(0,0)
        return max_money



# 回溯算法(选或不选)推导到朴素递归
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)

        # 返回值定为 i~n-1 的 max_money
        @cache
        def f(i):
            if i>=n:
                return 0

            # 选
            steal=f(i+2)+nums[i]
            # 不选
            skip=f(i+1)
            return max(steal,skip)

        return f(0)


# 动态规划
class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        dp=[0]*(n+2)
        for i in range(n-1,-1,-1): # n-1,n-2,...,2,1,0
            dp[i]=max(dp[i+1],dp[i+2]+nums[i])

        return dp[0]












