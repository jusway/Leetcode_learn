class Solution:
    def calculate(self, s: str) -> int:
        s=s.replace(" ","")
        stack=[]
        num=0
        pre_sign="+"

        n=len(s)
        for i in range(n):
            char=s[i]
            # 如果是数字
            if char.isdigit():
                num=num*10 + int(char)

            if not char.isdigit() or i==n-1: # 当前是运算符
                if pre_sign=="+":
                    stack.append(num)
                elif pre_sign=="-":
                    stack.append(-num)
                elif pre_sign == "*":
                    top=stack.pop()
                    plus=top*num
                    stack.append(plus)
                elif pre_sign=="/":
                    top=stack.pop()
                    divide=int(top/num)
                    stack.append(divide)

                pre_sign=char
                num=0

        return sum(stack)


class Solution1:
    # 不推荐，不使用栈的解法
    def calculate(self, s: str) -> int:
        if not s:
            return 0

        total_sum = 0  # 记录所有已经确定的加减结果总和
        prev_num = 0  # 记录上一个数字（等待被乘除法就地结算，或等待加到总和里）
        current_num = 0  # 动态解析当前遇到的数字
        op = '+'  # 记录上一个运算符，初始化为 '+'

        n = len(s)

        for i in range(n):
            char = s[i]

            # 1. 如果是数字，组合成完整的整数
            if char.isdigit():
                current_num = current_num * 10 + int(char)

            # 2. 如果遇到运算符，或者走到了字符串的末尾，就需要对“上一个数字”进行结算
            if (not char.isdigit() and char != ' ') or i == n - 1:
                if op == '+':
                    total_sum += prev_num  # 前一个数安全了，累加到总和
                    prev_num = current_num
                elif op == '-':
                    total_sum += prev_num  # 前一个数安全了，累加到总和
                    prev_num = -current_num
                elif op == '*':
                    prev_num = prev_num * current_num  # 乘法：就地结算
                elif op == '/':
                    # 注意：Python 的 // 对负数是向下取整，而题目要求向 0 取整（截断整数部分）
                    # 使用 int(a / b) 可以完美实现向 0 取整
                    prev_num = int(prev_num / current_num)

                op = char  # 更新运算符为当前遇到的符号
                current_num = 0  # 重置当前数字，为下一个数字做准备

        # 遍历结束后，把最后一个待结算的 prev_num 加上
        total_sum += prev_num

        return total_sum

if __name__ == '__main__':
    s=Solution()
    s.calculate("3+2*2")







