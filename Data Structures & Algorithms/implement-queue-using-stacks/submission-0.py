from collections import deque
class MyQueue:

    def __init__(self):
        self.stack1 = deque()
        self.stack2 = deque()

    def push(self, x: int) -> None:
        self.stack2.append(x)
        

    def pop(self) -> int:
        if len(self.stack1) == 0:
            while self.stack2:
                self.stack1.append(self.stack2.pop())

        return self.stack1.pop()
                
        

    def peek(self) -> int:
        if self.stack1:
            return self.stack1[-1]

        return self.stack2[0]

    def empty(self) -> bool:
        return len(self.stack1) + len(self.stack2) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()