from typing import List

from pip._internal.cli import main


class Solution1:
    # 超时
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=1
        while True:
            if i in nums:
                i=i+1
            else:
                return i


class Solution2:
    # 不符合常数额外空间
    def firstMissingPositive(self, nums: List[int]) -> int:
        num_sets = set(nums)
        i=1
        while True:
            if i in num_sets:
                i=i+1
            else:
                return i


class Solution:
    # 原地哈希
    def firstMissingPositive(self, nums: List[int]) -> int:
        i=0
        while i<len(nums):
            num=nums[i]
            if i==num-1: # 恰好归位
                i=i+1
            else: # 位置不对
                if 1<=num<=len(nums) and nums[nums[i] - 1] != nums[i]: # 有归位的资格 应该到 num-1 位置
                    # target=nums[num-1]
                    # nums[num - 1]=num
                    # nums[i]=target
                    # nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] # (1, 4) 错误
                    # nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] # (4, 1)
                    nums[num - 1], nums[i] = nums[i], nums[num - 1]
                else: # 没有归位资格的数
                    i=i+1

        # 再次遍历寻找那个值
        for i in range(len(nums)):
            if i==nums[i]-1:
                pass
            else:
                return i+1

        return len(nums)+1

if __name__ == '__main__':
    s=Solution()
    s.firstMissingPositive([1,1])




