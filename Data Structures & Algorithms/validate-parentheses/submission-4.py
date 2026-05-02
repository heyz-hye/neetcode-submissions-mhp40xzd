class Solution:
    def isValid(self, s: str) -> bool:
        map={'}':'{', ')' : '(', ']': '['}
        stack=[]

        for i in range(len(s)):
            if s[i] not in map:
                stack.append(s[i])
            if not stack:
                if s[i] in map:
                    return False
            if s[i] in map:
                if stack.pop()!=map[s[i]]:
                    return False
        return not stack

        