from collections import deque



class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        visited= [False]*n
        q= deque()
        q.append(0)
        visited[0]=True
        count=0

        while q:
            m=len(q)
            for _ in range(m):
                i=q.popleft()
                if i==n-1:
                    return count

                # 放进去 i 后面的元素
                for plus in range(1,nums[i]+1): # 如果nums[i]==3，那么 plus=1，2，3
                    j=i+plus
                    if j >= n:
                        break
                    if  not visited[j] :
                        q.append(j)
                        visited[j]=True

            count+=1



class Solution:
    def jump(self, nums: list[int]) -> int:
        n = len(nums)
        start=0
        end=0
        count=0

        while end<n-1:
            max_reach=0
            for i in range(start,end+1):
                max_reach=max(max_reach,i+nums[i])

            start=end+1
            end=max_reach
            count+=1

        return count



