from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        n = len(temperatures)
        answer = [0] * n

        for i in range(n):
            cur_temperature=temperatures[i]
            while True:
                # 比较当前温度和历史温度
                if stack and cur_temperature>temperatures[stack[-1]] : # 可以填写历史 对应答案
                    pre_idx=stack.pop()
                    answer[pre_idx]=i-pre_idx
                else:
                    break

            stack.append(i)

        return answer

if __name__ == '__main__':
    s=Solution()
    s.dailyTemperatures([73,74,75,71,69,72,76,73])