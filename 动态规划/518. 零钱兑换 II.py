from functools import cache


class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        n=len(coins)
        @cache
        def f(i,rest): # 在前i种硬币中选择 恰好凑成金额 rest 组合数量
            if rest==0:
                return 1
            if i==0:
                return 0

            if rest-coins[i-1]>=0:
                # 选
                a=f(i,rest-coins[i-1])
                # 不选
                b=f(i-1,rest)
                return a+b
            else:
                return f(i-1,rest)

        return f(n,amount)
