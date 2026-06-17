class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        current_num = 0

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append(current_num)
                current_num = 0  # 清空数字
                stack.append('[')
            elif char == ']':
                # str=""
                # while stack[-1]!="[":
                #     str=stack.pop()+str

                sub_strs = []
                while stack[-1] != "[":
                    sub_strs.append(stack.pop())

                # 循环结束后，一次性反转整个列表，复杂度是严格的 O(K)
                sub_strs.reverse()
                inner_str = "".join(sub_strs)

                stack.pop()

                repeat_time = stack.pop()

                stack.append(inner_str * repeat_time)

            else: # char是字母
                stack.append(char)

        return "".join(stack)

