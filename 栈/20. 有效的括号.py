





class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping = {")": "(", "]": "[", "}": "{"}
        for char in s:
            if char in {"(","[","{"}: # 左括号
                stack.append(char)
            else: # char 右括号
                if not stack: # 此时栈里边没有可以匹配的左括号了
                    return False

                # 此时栈里面是有元素的。
                top_ele=stack.pop()
                if mapping[char]!=top_ele: # 不匹配
                    return False

        if stack:
            return False
        else:
            return True

