from functools import cache


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        @cache
        def f(i): # 对于i位置 是否能够到达?
            if i==0:
                return True

            # 遍历 i 位置前面的所有位置（都有可能来到当前 i 位置）
            for k in range(i): # 0,1,...,i-1
                if nums[k]>=i-k and f(k): # k 位置有能力走到 i 位置
                    return True

            return False

        return f(len(nums)-1)

class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            # 遍历 i 位置前面的所有位置（都有可能来到当前 i 位置）
            for k in range(i):  # 0,1,...,i-1
                if nums[k] >= i - k and dp[k]:  # k 能到达，且有能力走到 i
                    dp[i] = True
                    break

        return dp[n - 1]

# 改写
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        dp = [False] * n
        dp[0] = True
        max_reach=nums[0]

        for i in range(1, n): # 1,2,...,n-1
            dp[i] = max_reach >= i          # 代替原来的内层循环
            if dp[i]:
                max_reach = max(max_reach, i + nums[i])  # 更新

        return dp[n - 1]



















# 贪心算法
class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        max_reach=nums[0]
        for i in range(1,n): # 1,2,...,n-1
            if i<=max_reach:
                max_reach=max(max_reach,i+nums[i])
            else:
                return False

        return True








