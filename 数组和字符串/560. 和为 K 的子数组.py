from typing import List


class Solution:
    # 前缀和+哈希表
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 构造前缀和
        pre_sum=[0]*(len(nums)+1)
        for i in range(len(nums)):
            pre_sum[i+1]=pre_sum[i]+nums[i]

        cache={} # 某些值出现了几次
        count=0
        for i,item in enumerate(pre_sum):
            other=item-k
            if other in cache:
                count+=cache[other]
            cache[item]=cache.get(item,0)+1

        return count

