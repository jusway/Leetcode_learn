from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]

        def is_palindrome(left, right) :
            while left<right:
                if s[left]!=s[right]:
                    return False
                left+=1
                right-=1
            return True

        def dfs(start_index):
            if start_index>=len(s):
                res.append(path.copy())
                return

            for i in range(start_index,len(s)):
                if is_palindrome(start_index,i):
                    path.append(s[start_index:i+1])
                    dfs(i+1)
                    path.pop()

        dfs(0)
        return res


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        path=[]

        def dfs(start_index,i):
            if start_index==len(s):
                res.append(path.copy())
                return
            if i == len(s):
                return

            # 要当前的字符而且判断下一个字符
            dfs(start_index,i+1)

            # 要当前的字符而且结束了
            tmp_str=s[start_index:i+1]
            if tmp_str==tmp_str[::-1]:
                path.append(tmp_str)
                dfs(i+1,i+1)
                path.pop()

        dfs(0,0)
        return res













