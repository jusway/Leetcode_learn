from typing import List


class Solution1:
    # 暴力破解
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,item in enumerate(nums):
            for j in range(i+1,len(nums)):
                post=nums[j]
                if item+post==target:
                    return [i,j]


class Solution2:
    # 利用哈希表
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        for i,item in enumerate(nums):
            cache[item]=i

        for i,item in enumerate(nums):
            other=target-item
            if other in cache and cache[other]!=i:
                return [i,cache[other]]

class Solution:
    # 哈希表进一步
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cache={}
        for i,item in enumerate(nums):
            other=target-item
            if other in cache:
                return [i,cache[other]]
            cache[item]=i

















