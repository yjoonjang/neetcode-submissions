from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        stack = []

        for ch in s:
            if ch in close_to_open:
                if stack and close_to_open[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        if stack:
            return False
        else:
            return True