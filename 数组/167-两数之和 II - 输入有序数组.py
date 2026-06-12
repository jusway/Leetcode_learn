from typing import List


class Solution1:
    # 哈希表传统解法
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        cache={}
        for i,item in enumerate(numbers):
            other=target-item
            if other in cache:
                return [cache[other]+1,i+1]
            cache[item]=i



class Solution:
    # 双指针
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        while not  left==right:
            my_sum=numbers[left]+numbers[right]
            if my_sum==target:
                return [left+1,right+1]
            elif my_sum>target:
                right-=1
            elif my_sum<target:
                left+=1

















