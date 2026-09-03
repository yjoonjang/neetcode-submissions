class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = ["+", "-", "*", "/"]
        stack = []
        result = 0

        for token in tokens:
            if token not in operators:
                stack.append(int(token))
            else: 
                first = stack.pop()
                second = stack.pop()
                if token == "+":
                    result = second + first
                    stack.append(result)
                elif token == "-":
                    result = second - first
                    stack.append(result)
                elif token == "*":
                    result = second * first
                    stack.append(result)
                else:
                    result = int(second / first)
                    stack.append(result)

        if len(stack) == 1:
            return stack.pop()
        return result
                
