from typing import List


class Solution:
    # 常规写法
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]

        def backtrack(cur_sum,start_index):
            if cur_sum==target:
                res.append(path.copy())
                return

            if cur_sum>target:
                return

            for i in range(start_index,len(candidates)):
                path.append(candidates[i])
                backtrack(cur_sum+candidates[i],i)
                path.pop()

        backtrack(0,0)
        return res


class Solution:
    # 排序，然后剪枝
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        candidates.sort()

        def backtrack(cur_sum,start_index):
            if cur_sum==target:
                res.append(path.copy())
                return


            for i in range(start_index,len(candidates)):
                if cur_sum + candidates[i] > target:
                    break
                path.append(candidates[i])
                backtrack(cur_sum+candidates[i],i)
                path.pop()

        backtrack(0,0)
        return res


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        candidates.sort()

        def dfs(i,cur_sum):
            if cur_sum == target:
                res.append(path.copy())
                return

            if i >= len(candidates):
                return

            if cur_sum+candidates[i]>target:
                return

            path.append(candidates[i])
            dfs(i,cur_sum+candidates[i])
            path.pop()

            dfs(i+1,cur_sum)


        dfs(0,0)
        return res















