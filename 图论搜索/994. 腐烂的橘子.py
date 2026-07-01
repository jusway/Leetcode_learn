from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        queue=deque()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # 统计一共多少新鲜橘子
        fresh_count=0
        for row in range(rows):
            for column in range(columns):
                cur_num=grid[row][column]
                if cur_num==2:
                    queue.append((row,column))
                elif cur_num==1 :
                    fresh_count+=1

        minutes=0

        if len(queue)==0 and fresh_count==0:
            return 0

        while queue:
            size=len(queue)
            for _ in range(size): # 管理当前层（轮）的遍历和处理
                row,column=queue.popleft()

                for dx,dy in directions:
                    next_row=row+dx
                    next_column=column+dy

                    # 越界
                    if next_row<0 or next_row>=rows or next_column<0 or next_column>=columns:
                        continue

                    # 不是新鲜橘子
                    if grid[next_row][next_column]!=1:
                        continue

                    grid[next_row][next_column]=2
                    fresh_count-=1
                    queue.append((next_row,next_column))

            minutes+=1

        if fresh_count>0:
            return -1

        return minutes-1

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue=deque()
        minutes=0

        # 统计一共多少新鲜橘子
        fresh_count=0
        for row in range(rows):
            for column in range(columns):
                cur_num=grid[row][column]
                if cur_num==1 :
                    fresh_count+=1
                elif cur_num==2:
                    queue.append((row,column))


        while queue and fresh_count > 0:
            size=len(queue)
            for _ in range(size):
                row,column=queue.popleft()
                for dx,dy in directions:
                    next_row=row+dx
                    next_column=column+dy

                    # 越界
                    if next_row<0 or next_row>=rows or next_column<0 or next_column>=columns:
                        continue

                    # 不是新鲜橘子
                    if grid[next_row][next_column]!=1:
                        continue

                    grid[next_row][next_column]=2
                    fresh_count-=1
                    queue.append((next_row,next_column))

            minutes+=1

        if fresh_count>0:
            return -1

        return minutes

















