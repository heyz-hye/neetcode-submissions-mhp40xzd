class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        a=0
        b=0
        if tokens:
            for s in tokens:
                if s=='+':
                    a=stack.pop()
                    b=stack.pop()
                    ans=int(a)+int(b)
                    stack.append(ans)
                elif s=='-':
                    a=stack.pop()
                    b=stack.pop()
                    ans=int(b)-int(a)
                    stack.append(ans)
                elif s=='/':
                    a=stack.pop()
                    b=stack.pop()
                    ans=int(b)/int(a)
                    stack.append(int(ans))
                elif s=='*':
                    a=stack.pop()
                    b=stack.pop()
                    ans=int(a)*int(b)
                    stack.append(ans)
                else:
                    stack.append(s)
        return int(stack[-1])


        