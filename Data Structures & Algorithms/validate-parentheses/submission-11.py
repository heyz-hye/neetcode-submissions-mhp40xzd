class Solution:
    def isValid(self, s: str) -> bool:
        smap={'}':'{', ')' : '(', ']': '['}
        stack=[]

        for i in s:
            if i in smap:
                if stack and stack[-1]==smap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return not stack
