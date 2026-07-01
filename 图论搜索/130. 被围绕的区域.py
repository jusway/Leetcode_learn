from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        columns=len(board[0])

        def dfs(row,column): # 把所有 O 标记为 #
            # 边界越界
            if row<0 or row>=rows or column<0 or column>= columns:
                return

            # # 如果当前是 X，不关注
            # if board[row][column]=="X":
            #     return
            # if board[row][column]=="#":
            #     return
            if board[row][column]!="O":
                return

            board[row][column]="#"

            dfs(row-1,column)
            dfs(row+1,column)
            dfs(row,column-1)
            dfs(row,column+1)


        # 遍历所有边界
        for row in range(rows):
            if board[row][0]=="O":
                dfs(row,0)
            if board[row][columns-1]=="O":
                dfs(row,columns-1)

        for column in range(columns):
            if board[0][column]=="O":
                dfs(0,column)
            if board[rows-1][column]=="O":
                dfs(rows-1,column)


        # 遍历所有网格，把井号替换成圈儿，把圈儿替换成叉
        for row in range(rows):
            for column in range(columns):
                if board[row][column]=="#":
                    board[row][column]="O"
                elif board[row][column]=="O":
                    board[row][column]="X"







