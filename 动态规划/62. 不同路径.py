


from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        @cache
        def f(i,j): # 从(0,0)走到(i,j)的 路径个数
            if i==0 and j==0:
                return 1
            if i==-1:
                return 0
            if j==-1:
                return 0


            return f(i-1,j)+f(i,j-1)

        return f(m-1,n-1)


# dp
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0]*(n+1) for _ in range(m+1)] # m+1行，n+1列
        dp[0][0]=1
        for i in range(0,m): # 0,1,2,3,...,m-1
            for j in range(0,n): # 0,1,2,...,n-1
                if i==0 and j==0:
                    continue
                dp[i][j]= dp[i - 1][ j] + dp[i][ j - 1]

        return dp[m-1][n-1]


from math import comb
# 彩蛋。不通用的解法
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return comb(m + n - 2, m - 1)











