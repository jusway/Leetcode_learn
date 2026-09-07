from typing import List


class Solution:
    # 邻接矩阵如何进行dfs连通块标记法？
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        visited = [False] * n

        def dfs(i):
            if visited[i]:
                return

            visited[i] = True
            for j in range(n):
                if isConnected[i][j] == 1:
                    dfs(j)

        count = 0
        for i in range(n):
            if not visited[i]:
                count += 1
                dfs(i)

        return count
