from typing import List


class NumArray1:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def sumRange(self, left: int, right: int) -> int:
        my_sum=0
        for i in range(left,right+1):
            my_sum+=self.nums[i]

        return my_sum


class NumArray:

    def __init__(self, nums: List[int]):
        self.preSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            self.preSum[i+1]=self.preSum[i]+nums[i]

    def sumRange(self, left: int, right: int) -> int:
        # 时间复杂度：O(1)
        return self.preSum[right+1]-self.preSum[left]











if __name__ == '__main__':
    a=NumArray([0,1,2,3,4,5,6])
    print(a.sumRange(0, 2))