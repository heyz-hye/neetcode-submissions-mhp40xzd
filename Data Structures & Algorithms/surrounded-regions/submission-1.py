'''
first approach is to use a bfs and add all o to the queue and the visited set and if the the o is enclose by
another o and Xs it is surrounded.
bad solution:
because there can be a bunch of o that is surround by x and one o that is connected to the o is touching the border making it
a not surrounded. To be consider surrounded all o that is connected or singular need to be surrounded by x

try seeding from border approach again
check letter o from border and another node connected to it
then put those index in a set and turn any o that isnt in the set into x
'''

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visit=set()
        q=deque()
        direction=[[1,0],[0,1],[-1,0],[0,-1]]
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c]=="O" and (r==0 or c==0 or r==len(board)-1 or c==len(board[0])-1):
                    q.append([r,c])
                    visit.add((r,c))

        while q:
            for num in range(len(q)):
                row,col=q.popleft()
              
                for t in range(len(direction)):
                    rw=row+direction[t][0]
                    cl=col+direction[t][1]
                    if rw<0 or rw==len(board) or cl<0 or cl==len(board[0]) or (rw,cl) in visit or board[rw][cl]=="X":
                        continue
                    else:
                        visit.add((rw,cl))
                        q.append([rw,cl])
        
        for ro in range(len(board)):
            for co in range(len(board[0])):
                if board[ro][co]=="O" and (ro,co) not in visit:
                    board[ro][co]="X"
        