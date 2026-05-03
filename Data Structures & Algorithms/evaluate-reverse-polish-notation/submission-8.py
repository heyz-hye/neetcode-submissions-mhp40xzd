class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        
        if tokens:
            for s in tokens:
                if s == '+':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)
                elif s == '-':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)  # Flipped!
                elif s == '*':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)
                elif s == '/':
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a)) # Flipped and truncated!
                else:
                    # Cast to int exactly once here
                    stack.append(int(s))
                    
        return stack[-1]
        