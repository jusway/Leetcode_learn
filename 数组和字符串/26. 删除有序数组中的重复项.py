from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read=0
        write=0
        while read<len(nums):
            if nums[read]==nums[write]:
                read+=1
            else:
                write+=1
                nums[write]=nums[read]

        return write+1