

# 回溯算法的思路
class Solution:
    def climbStairs(self, n: int) -> int:
        path=[]
        count=0

        def back_tracking(cur_sum):
            nonlocal count
            if cur_sum==n:
                count+=1
                return
            if cur_sum>n:
                return

            for step in (1,2):
                path.append(step)
                cur_sum+=step
                back_tracking(cur_sum)

                # 回溯
                path.pop()
                cur_sum-=step

        back_tracking(0)
        return count

# 去掉 path
class Solution:
    def climbStairs(self, n: int) -> int:
        count=0
        def back_tracking(cur_stair):
            nonlocal count
            if cur_stair==n:
                count+=1
                return
            if cur_stair>n:
                return

            for step in (1,2):
                cur_stair+=step
                back_tracking(cur_stair)

                # 回溯
                cur_stair-=step

        back_tracking(0)
        return count

# 计算方法个数，找到了递推公式，分解为子问题
class Solution:
    def climbStairs(self, n: int) -> int:
        def f(x): # 0~x 台阶的方法个数
            if x==0:
                return 1
            if x==1:
                return 1

            return f(x-1)+f(x-2)

        return f(n)

# 缓存查表(记忆化搜索)
class Solution:
    def climbStairs(self, n: int) -> int:
        memory={}

        def f(x): # 从0走到 x 台阶的方法个数
            if x==0:
                return 1
            if x==1:
                return 1
            if x in memory:
                return memory[x]

            ways_number=f(x - 1) + f(x - 2)
            memory[x]=ways_number
            return ways_number

        return f(n)


# 使用Python的库
from functools import cache
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def f(x): # 从开始走到 x 台阶的方法个数
            if x==0:
                return 1
            if x==1:
                return 1

            return f(x-1)+f(x-2)

        return f(n)

# 动态规划
class Solution:
    def climbStairs(self, n: int) -> int:
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,n+1): #  2,3,4,...,n-1,n
            dp[i]=dp[i-1]+dp[i-2]

        return dp[n]


# 滚动数组




