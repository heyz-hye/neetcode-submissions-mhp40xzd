'''
first approach is to use a bfs and add all o to the queue and the visited set and if the the o is enclose by
another o and Xs it is surrounded.
bad solution:
because there can be a bunch of o that is surround by x and one o that is connected to the o is touching the border making it
a not surrounded. To be consider surrounded all o that is connected or singular need to be surrounded by x

try seeding from border approach again
check letter o from border and another node connected to it
then put those index in a set and turn any o that isnt in the set into x
you can do both bfs and dfs

time complexity for this:
mxn you bfs trhough the entire board in 4 directions
space complexity:
mxn your visit set hold every index

there is a way to optimize space complexity:
let each boarder O and its connect nodes turn into a temporary value
when the loop finish, you check for any remaining O turn it into X
and then turn the temporary value back into O

'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def dfs(r,c):
            if r<0 or c<0 or r==len(board) or c==len(board[0]) or board[r][c]!="O":
                return
            
            board[r][c]="T"

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="O" and (r==0 or c==0 or r==len(board)-1 or c==len(board[0])-1):
                    dfs(r,c)

        for ro in range(len(board)):
            for co in range(len(board[0])):
                if board[ro][co]=="O":
                    board[ro][co]="X"
                if board[ro][co]=="T":
                    board[ro][co]="O"
        