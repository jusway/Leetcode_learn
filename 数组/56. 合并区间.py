from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 先排序
        # def get_start_num(nums):
        #     return nums[0]
        # intervals.sort(key=get_start_num)
        # lambda表达式排序
        intervals.sort(key=lambda x: x[0])
        # 再合并

        res = []
        i=0
        cur = intervals[0]
        while i+1<len(intervals):
            next=intervals[i+1]
            if cur[1]>=next[0]: # 重叠
                cur[1]=max(cur[1],next[1])
            else: # 不重叠
                res.append(cur)
                cur=next
            i=i+1
        res.append(cur)

        return res



if __name__ == '__main__':
    s=Solution()
    s.merge([[1,3],[2,6],[8,10],[15,18]])


