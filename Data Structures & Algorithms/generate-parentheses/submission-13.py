'''
In this decision tree we always need with open parenthesis to be valid
after that we can always choose to append open parenthesis or close parenthesis
if the open parenthesis is less than n which is the target we can always append
if the close parenthesis is less than open parenthesis we can always append it
for the function we are going to pass in parenthesis and the count of each type of
parenthesis. We pass in each type becauese the variabe counto and countc is non-local
and we have manually decrement them more than we need it to like everytime we pop we gotta
decrement one of the count for parenthesis..
when you find a valid string that have equal amount of open parenthesis
and equal amount of close parenthesis that match the target n we join the character in a str
and append to it to the res list
in conclusion
there can be only 3 states in our decision tree after initlizing with open parenthesis, one
of them is op<n which mean we can still append open parenthesis, you can have more than open 
than close that mean you can append close parenthesis, the last is where you found the solution
where open and close is equal and you can join to append to resolution
On  recrusive call we need to subset.pop() to backtrack 
the run time is 2^N and space is O(N) depth of the search

my mistakes:
i did subset.pop()after every single recursive call this pop the child parenthesis and the
parent parenthesis, if we pop parent parenthesis too early we miss the decision tree part without
the exploring the other option, every call is restored to it previous state when return
therefore each call is responsible for cleaning up its own mess.
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
               
            
            if op<n:
                dfs("(",op,cl)
            subset.pop() #backtrack return to original state
            
        dfs("(",0,0)
        return self.res

        