from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # 比如 n=4 时，nums = [1, 2, 3, 4]
        nums = [i for i in range(1, n + 1)]
        result = []
        path=[]
        def backtrack(start_index):
            if len(path) == k:
                result.append(path[:])  # 深拷贝
                return

            for i in range(start_index, len(nums)):
                path.append(nums[i])  # 做选择
                backtrack( i + 1)  # 递归：传递下一个下标和 path
                path.pop()  # 撤销选择（回溯）

        backtrack(0 )
        return result



class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        path=[]
        def backtrack(start_num):
            if len(path)==k:
                res.append(path[:])
                return

            for num in range(start_num,n+1):
                path.append(num)
                backtrack(num+1)
                path.pop()


        backtrack(1)
        return res




class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        path=[]
        def backtrack(cur_num):
            if len(path) == k:
                res.append(path[:])  # 深拷贝
                return

            if cur_num > n:
                return

            # 选
            path.append(cur_num)
            backtrack(cur_num+1)
            # 回溯
            path.pop()
            # 不选
            backtrack(cur_num+1)

        backtrack(1)
        return res









