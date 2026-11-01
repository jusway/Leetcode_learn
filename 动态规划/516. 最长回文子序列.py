from functools import cache


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        @cache
        def f(i,j): # i~j范围中 最长回文子序列的长度
            if i==j:
                return 1
            if i>j:
                return 0

            if s[i]==s[j]:
                return f(i+1,j-1)+2
            else:
                # j 位置字符不在要找的回文子序列中
                a= f(i,j-1)
                # i 位置字符不在要找的回文子序列中
                b=f(i+1,j)
                return max(a,b)

        return f(0,n-1)


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for _ in range(n)]
        for k in range(n):
            dp[k][k]=1

        for i in range(n-2,-1,-1): # n-2,n-3,...,1,0
            for j in range(i+1,n): # i+1,i+2,...,n-1
                if s[i] == s[j]:
                    dp[i][j]= dp[i + 1][ j - 1] + 2
                else:
                    # i 位置字符不在要找的回文子序列中
                    a = dp[i + 1][ j]
                    # j 位置字符不在要找的回文子序列中
                    b = dp[i][ j - 1]
                    dp[i][j]=  max(a, b)

        return dp[0][n-1]


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [0] * n

        for i in range(n - 1, -1, -1):
            dp[i] = 1      # 对角线 dp[i][i] = 1
            pre = 0        # 记录左下角 dp[i+1][i]
            for j in range(i + 1, n):
                tmp = dp[j]                # 存一下 dp[i+1][j]，下一轮它就是左下角
                if s[i] == s[j]:
                    dp[j] = pre + 2        # pre 是 dp[i+1][j-1]
                else:
                    dp[j] = max(dp[j], dp[j - 1])  # 正下方（旧）、正左方（新）
                pre = tmp

        return dp[n - 1]

