class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque() #deque is a method
        direction=[[1,0],[0,1],[0,-1],[-1,0]]
        dist=0
        visit=set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    q.append((r,c))
        
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                grid[row][col]=dist

                for r, c in direction:
                    rw=row+r
                    cl=col+c
                    if rw>=len(grid) or cl>=len(grid[0]) or rw<0 or cl<0 or grid[rw][cl]!=2147483647 or (rw,cl) in visit:
                        continue
                    q.append((rw,cl))
                    visit.add((rw,cl))
            dist+=1