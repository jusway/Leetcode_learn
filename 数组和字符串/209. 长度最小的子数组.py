from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        slow=0
        fast=0
        my_sum=0
        min_len=float("inf")
        while fast<len(nums):
            my_sum+=nums[fast]
            while my_sum>=target:
                min_len=min(min_len,fast-slow+1)
                my_sum-=nums[slow]
                slow+=1

            fast+=1

        return min_len if min_len!=float("inf") else 0