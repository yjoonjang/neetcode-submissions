class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []
        # self.minimum = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if self.minimum is None or (self.minimum is not None and self.minimum > val):
        if len(self.min_stack) == 0 or self.min_stack[-1] >= val:
            self.min_stack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if x == self.min_stack[-1]:
            # if len(self.stack) == 0:
            #     self.minimum = None
            # else:
            #     self.minimum = min(self.stack)
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_stack[-1]
        
