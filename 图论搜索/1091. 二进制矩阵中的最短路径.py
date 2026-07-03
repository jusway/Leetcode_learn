from collections import deque
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0]!=0:
            return -1

        rows=len(grid)
        columns=len(grid[0])
        queue=deque()
        directions=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

        # 初始化队列
        queue.append((0,0))
        grid[0][0]=1
        count=1

        while queue :
            size=len(queue)
            for _ in range(size):
                x,y=queue.popleft()
                if x==rows-1 and y==columns-1:
                    return count

                for dx,dy in directions:
                    next_x=x+dx
                    next_y=y+dy

                    if next_x<0 or next_x>=rows or next_y<0 or next_y>=columns:
                        continue

                    if grid[next_x][next_y]!=0:
                        continue

                    grid[next_x][next_y]=1
                    queue.append((next_x,next_y))

            count+=1

        return -1











