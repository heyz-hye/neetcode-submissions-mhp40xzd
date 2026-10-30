class Solution:
    def isValid(self, s: str) -> bool:
        table={'}':'{', ')' : '(', ']': '['}
        stack=[]
        
        for i in s:
            if i not in table:
                stack.append(i)

            elif stack and table[i]==stack[-1]:
                stack.pop()
            
            else:
                return False
        
        if stack:
            return False
        else:
            return True
                
