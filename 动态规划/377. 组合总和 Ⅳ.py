from functools import cache


class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        n=len(nums)
        @cache
        def f(x): # 总和恰好为x  方法数量
            if x==0:
                return 1

            res=0
            for i in range(n):
                if x-nums[i]>=0:
                    res += f(x - nums[i])

            return res

        return f(target)


