class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q=deque() #deque is a method
        fresh=0
        direction=[[1,0],[0,1],[0,-1],[-1,0]]
        time=0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    fresh+=1
                if grid[r][c]==2:
                    q.append((r,c))
               
        while q and fresh:
            for i in range(len(q)): #if time is in the for loop we increment time on length of q which is not right
                row,col=q.popleft()
                

                for r,c in direction:
                    rw=row+r
                    cl=col+c
                    if rw>=len(grid) or cl>=len(grid[0]) or rw<0 or cl<0 or grid[rw][cl]!=1:
                        continue
                    q.append((rw,cl))
                    fresh-=1 #we also need to decrement fresh or else we always return -1 because fresh never deremented properly
                    grid[rw][cl]=2
            time+=1
        if not fresh:
            return time
        if not q:
            return -1

                
