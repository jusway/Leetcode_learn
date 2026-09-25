


from functools import cache

class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        @cache
        def f(i): # 0~i范围 以i结尾的 最长的严格递增子序列的长度
            if i==0:
                return 1

            max_length=1
            for j in range(0,i): # 以 0,1,2,...,i-1 结尾的最长的递增子序列的长度
                if nums[i]>nums[j]: # 严格递增！
                    i_length=f(j)+1
                    max_length=max(max_length,i_length)

            return max_length

        return max(f(i) for i in range(n)) # max(f0,f1,...,fn-1)


# dp数组动态规划
class Solution:
    def lengthOfLIS(self, nums: list[int]) -> int:
        n=len(nums)
        dp=[1]*n
        for i in range(1,n): # 1,2,3,...,n-1
            max_length = 1
            for j in range(0, i):  # 以 0,1,2,...,i-1 结尾的最长的递增子序列的长度
                if nums[i] > nums[j]:  # 严格递增！
                    i_length = dp[j] + 1
                    max_length = max(max_length, i_length)

            dp[i]= max_length

        return max(dp)














