class Solution:
    def sum(self, num1: int, num2: int) -> int:
        return num1+num2

if __name__ == '__main__':
    s=Solution()
    ans=s.sum(12,5)
    assert ans==17, "错了！！！"
