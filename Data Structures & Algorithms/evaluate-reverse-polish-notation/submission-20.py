class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = ["+", "-", "*", "/"]
        stack = deque(tokens)
        num_stack = []

        while stack:
            token = stack.popleft()
            if token in operations:
                n2 = num_stack.pop()
                n1 = num_stack.pop()
                if token == "+":
                    output = n1 + n2
                elif token == "-":
                    output = n1 - n2
                elif token == "*":
                    output = n1 * n2
                elif token == "/":
                    output = int(n1 / n2)
                num_stack.append(output)
            else:
                num_stack.append(int(token))
        
        if len(num_stack) == 1:
            return num_stack[0]
        else:
            return output


