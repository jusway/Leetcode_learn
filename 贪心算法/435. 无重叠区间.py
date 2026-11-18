from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x: x[0])
        pre_start,pre_end=intervals[0]
        count=0

        for i in range(1,n): # 1,2,...,n-1
            cur_start,cur_end=intervals[i]
            if pre_end>cur_start: # 重叠
                count+=1
                if pre_end>cur_end:
                    pre_start, pre_end=cur_start,cur_end
                else:
                    pass
            else:  # 没重叠
                pre_start, pre_end=cur_start,cur_end

        return count

# 小优化
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x: x[0])
        pre_end=intervals[0][1]
        count=0

        for i in range(1,n): # 1,2,...,n-1
            cur_start,cur_end=intervals[i]
            if pre_end>cur_start: # 重叠
                count+=1
                if pre_end>cur_end:
                    pre_end=cur_end
            else:  # 没重叠
                pre_end=cur_end

        return count


# 右端点排序
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        n=len(intervals)
        intervals.sort(key=lambda x: x[1])
        pre_end=intervals[0][1]
        count=0

        for i in range(1,n): # 1,2,...,n-1
            cur_start,cur_end=intervals[i]
            if pre_end<=cur_start: # 不重叠
                pre_end=cur_end
            else:
                count+=1


        return count



















