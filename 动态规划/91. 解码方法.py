from functools import cache


class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        VALID = {str(x) for x in range(10, 27)}  # {"10","11",...,"26"}
        @cache
        def f(i): #  字符串s 0~i 范围的解码方法个数
            if i==-1:
                return 1

            if i==0:
                if s[0]!="0":
                    return 1
                else:
                    return 0

            # 解码一个字符的情况
            if s[i] !="0":
                one=f(i-1)
            else:
                one=0

            # 解码两个字符的情况
            if s[i-1:i+1] in VALID:
                two=f(i-2)
            else:
                two=0

            return one+two

        return f(n-1)


# 动态规划
class Solution:
    def numDecodings(self, s: str) -> int:
        n=len(s)
        dp=[0]*(n+1)
        dp[-1]=1
        if s[0] != "0":
            dp[0]=1
        else:
            dp[0]=0
        VALID = {str(x) for x in range(10, 27)}  # {"10","11",...,"26"}

        for i in range(1,n): # 1,2,3,...,n-2,n-1
            # 解码一个字符的情况
            if s[i] != "0":
                one = dp[i - 1]
            else:
                one = 0

            # 解码两个字符的情况
            if s[i - 1:i + 1] in VALID:
                two = dp[i - 2]
            else:
                two = 0

            dp[i]=one+two

        return dp[n-1]











