'''
we can keep track of left parenthesis, we can also use an hashmap, if 
the parenthesis the opening part or the closing part more than the n you return
in a decision you can choose to take the opening or clos
edge you can never have a close parenthesis at the beginning
'''
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.res=[]
        subset=[]
        if n<1:
            return self.res
        def dfs(paren,op,cl):
            if paren=="(":
                op+=1
                subset.append(paren)
            else:
                cl+=1
                subset.append(paren)
            
            if op==n and cl==n:
                self.res.append("".join(subset))
                subset.pop()
                return
            
            if op>cl:
                dfs(")",op,cl)
               
            
            if op>n:
                subset.pop()
                return
            else:
                dfs("(",op,cl)
            subset.pop()
            
        dfs("(",0,0)
        return self.res

        