from functools import cache


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)

        @cache
        def f(i): # 0~i范围 以i为结尾的 连续子数组的最大和
            if i==0:
                return nums[0]

            f_i_1=f(i-1)
            if f_i_1>0: # 有帮助
                return f_i_1+nums[i]
            else: # 没帮助
                return nums[i]

        return max(f(i) for i in range(n)) # max(f0,f1,f2,...,fn-1)


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)

        @cache
        def f(i): # 0~i范围 以i为结尾的 连续子数组的最大和
            if i==0:
                return nums[0]

            # 这个连续子数组很长(>=2)
            a=f(i-1)+nums[i]
            # 这个连续子数组==1个
            b=nums[i]

            return max(a,b)

        return max(f(i) for i in range(n)) # max(f0,f1,f2,...,fn-1)


# 动态规划
class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[0]*n
        dp[0]=nums[0]

        for i in range(1,n): # 1,2,3,...,n-1
            # 这个连续子数组很长(>=2)
            a = dp[i - 1] + nums[i]
            # 这个连续子数组==1个
            b = nums[i]
            dp[i] =max(a, b)

        return max(dp)













