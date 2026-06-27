from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res=[]
        path=[]
        candidates.sort()

        def dfs(start_index,cur_sum):
            if cur_sum==target:
                res.append(path.copy())
                return


            for i in range(start_index,len(candidates)):
                if cur_sum+candidates[i]>target:
                    break
                if i>start_index and candidates[i]==candidates[i-1]: # 去重
                    continue
                path.append(candidates[i])
                dfs(i+1,cur_sum+candidates[i])
                path.pop()

        dfs(0,0)
        return res
