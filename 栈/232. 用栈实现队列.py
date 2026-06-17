class MyQueue:

    def __init__(self):
        self.in_stack=[]
        self.out_stack=[]

    def push(self, x: int) -> None:
        self.in_stack.append(x)


    def pop(self) -> int:
        if self.out_stack:
            return self.out_stack.pop()
        else: # 出栈里面没东西了
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())

            return self.out_stack.pop()


    def peek(self) -> int:
        if self.out_stack:
            return self.out_stack[-1]
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop())
            return self.out_stack[-1]


    def empty(self) -> bool:
        if self.in_stack or  self.out_stack:
            return False
        else:
            return True

# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()