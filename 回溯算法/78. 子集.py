from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]


        def backtrack(start_index):
            res.append(path.copy())

            if start_index>=len(nums):
                return

            for i in range(start_index,len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        path=[]

        def dfs(i):
            if i>=len(nums):
                res.append(path.copy())
                return

            # 选
            path.append(nums[i])
            dfs(i+1)
            # 回溯
            path.pop()
            # 不选
            dfs(i+1)

        dfs(0)
        return res










