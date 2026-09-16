from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            # "(": ")",
            ")": "(",
            # "{": "}",
            "}": "{",
            # "[": "]",
            "]": "["
        }

        stack = []
        
        for ch in s:
            if ch in pairs:
                if stack and pairs[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        
        if stack:
            return False
        else:
            return True
            