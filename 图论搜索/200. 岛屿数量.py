from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows=len(grid)
        columns=len(grid[0])
        count=0


        def dfs(row,column): # 展开递归，为了把这片岛屿全部淹没
            # 边界越位
            if row<0 or row>=rows or column<0 or column >=columns:
                return
            # 遇到水
            if grid[row][column]=="0":
                return

            # 遇到陆地，进行操作，淹没陆地
            grid[row][column] = "0"

            dfs(row-1,column)
            dfs(row+1,column)
            dfs(row,column-1)
            dfs(row,column+1)

        for row in range(rows):
            for column in range(columns):
                if grid[row][column]=="1":
                    count+=1
                    dfs(row,column)

        return count













