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


class Solution:
    # 标签合并法(初级并查集)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        labels=list(range(n)) # [0,1,2,3,4,5,6]
        count=n

        # 遍历所有边，然后一个个合并标签
        for i in range(n):
            for j in range(i+1,n): # 因为是对称矩阵，所以只需要遍历上三角形
                # 如果i和j节点没有边存在，那么跳过
                if isConnected[i][j]==0:
                    continue
                # 接下来是i和j节点存在边的情况
                # 虽然存在边，但是如果两个节点已经划归为同一类的话，那也什么也不做直接跳过
                if labels[i]==labels[j]:
                    continue
                # 接下来是i和j节点存在边而且确实不同类，可以着手合并了
                keep,drop=labels[i],labels[j]
                for k in range(n):
                    if labels[k]==drop:
                        labels[k]=keep
                count-=1

        return count


# 抽象成类的“初级并查集”
class UnionFind:
    # 把上面标签合并法的逻辑原封不动搬进类里，合并依然是 O(n) 的扫全表改标签
    def __init__(self,n):
        # labels[i] 就是 i 的类别标签，初始时每个节点自己一类
        self.labels=list(range(n))
        # 当前有多少类，每成功合并一次就减一
        self.count=n

    def find(self,x):
        # 标签就直接代表所属集合，一步就能拿到，不用往上爬
        return self.labels[x]

    def union(self,x,y):
        keep,drop=self.labels[x],self.labels[y]
        # 标签相同说明本来就是一类，什么都不用做
        if keep==drop:
            return False
        # 确实不同类，把所有 drop 标签的节点都改成 keep
        for k in range(len(self.labels)):
            if self.labels[k]==drop:
                self.labels[k]=keep
        self.count-=1
        return True

class Solution:
    # 并查集类解法(内部仍是标签合并法)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        uf=UnionFind(n)

        # 依然只遍历上三角，遇到边就合并，合并的细节全部交给并查集
        for i in range(n):
            for j in range(i+1,n):
                if isConnected[i][j]==1:
                    uf.union(i,j)

        # 剩下几类，就是几个省份
        return uf.count






