'''
we need to traverse the matrix in a for loop
the for loop will check every single index for the matrix
the for loop will also check in dfs that there is a route that you can take to
that can find the target word. every single call you make you are passing in the index
of the word so you match the letter of the word to the 4 different directional calls.
if the the index that the recrusive call called doesnt exist it return false
if the index doesnt match the letter for the word it also return false
for every single index we call recrusively from we will mark it with hashtag so we dont have to search it again
that cut down the calls to 3 different directional call since one will always return to the original call index
when we return false, we backtrack and return the current index to the previous state so that it can be apart
of another recursive scan from another index down the for loop.
the process will be loop through the indexes and scanning each index
looping will be done by the exist function
and scanning will be done by the dfs function

Question:how does i==len(word return True for all the calls), shouldn't you do word[i]==board[r][c]
It all comes down to how the or operators propagate a True value back up the "call stack," and why checking word[i] == board[r][c] -> return True too early would actually break the algorithm.

Here is exactly how it works:
1. How True bubbles all the way up

When the code evaluates the recursive calls, it chains them together with or:
Python

res = dfs(i + 1, ...) or dfs(i + 1, ...) or dfs(i + 1, ...) or dfs(i + 1, ...)

In Python, the or operator uses short-circuit evaluation. This means if any of those dfs calls returns True, the entire expression immediately evaluates to True, ignores the remaining directions, and assigns True to res.
'''
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i,row,col) ->bool:

            if i==len(word): # this statement have to sit above the word[i]!=board[row][col] because this statement will throw index out of bound error
                            #and we never get to return true statement
                return True
            if row<0 or col <0 or row>=len(board) or col>=len(board[0]) or word[i]!=board[row][col]:
                return False

            temp=board[row][col]
            board[row][col]="#" #this avoid overhead call checking the same element again

            res=dfs(i+1,row+1,col) or dfs(i+1,row-1,col) or dfs(i+1,row,col+1) or dfs(i+1,row,col-1) #if any of the exploration match we keep going that is why we use or
            #we increment i every time to find the next match with the next letter in word
            board[row][col]=temp #backtrack here

            return res
        for r in range(len(board)):
            for c in range(len(board[0])):
                if dfs(0,r,c):
                    return True
        return False
        