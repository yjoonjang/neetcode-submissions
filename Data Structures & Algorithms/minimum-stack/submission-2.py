class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minimum is None or (self.minimum is not None and self.minimum > val):
            self.minimum = val

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.minimum:
            if len(self.stack) == 0:
                self.minimum = None
            else:
                self.minimum = min(self.stack)

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.minimum
        
