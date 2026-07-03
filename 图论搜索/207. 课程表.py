from collections import deque
from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 构造邻接表
        graph=[ [] for _ in range(numCourses) ]
        # 构造入度表
        indegree=[0]*numCourses
        # 遍历边列表
        for after,pre in prerequisites:
            graph[pre].append(after)
            indegree[after]+=1

        # 初始化
        queue=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                queue.append(i)

        while queue:
            cur_class = queue.popleft()
            for after in  graph[cur_class]:
                indegree[after]-=1
                if indegree[after]==0:
                    queue.append(after)

        for item in indegree:
            if item!=0:
                return False

        return True









