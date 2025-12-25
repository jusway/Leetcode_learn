from typing import List


class Solution1:
    # 常规法
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat= [[0]*n for _ in range(n)]
        count=1
        start_index=0 # 0,0
        while not count>=n**2:
            for j in range(start_index,n-1-start_index):
                mat[start_index][j]=count
                count+=1
            for i in range(start_index,n-1-start_index):
                mat[i][n-1-start_index]=count
                count+=1
            for j in range(n-1-start_index,start_index,-1):
                mat[n-1-start_index][j]=count
                count+=1
            for i in range(n-1-start_index,start_index,-1):
                mat[i][start_index]=count
                count+=1

            start_index+=1

        if n%2==1:
            mat[n//2][n//2]=count

        return mat

class Solution:
    # 边界收缩法（撞南墙法）
    def generateMatrix(self, n: int) -> List[List[int]]:
        mat = [[0] * n for _ in range(n)]
        top, bottom = 0, n - 1
        left, right = 0, n - 1
        count = 1
        while count<=n**2:
            for j in range(left,right+1):
                mat[top][j]=count
                count+=1
            top+=1
            for i in range(top, bottom + 1):
                mat[i][right] = count
                count += 1
            right -= 1
            for j in range(right, left - 1, -1):
                mat[bottom][j] = count
                count += 1
            bottom -= 1
            for i in range(bottom, top - 1, -1):
                mat[i][left] = count
                count += 1
            left += 1

        return mat



























if __name__ == '__main__':
    s=Solution()
    s.generateMatrix(5)