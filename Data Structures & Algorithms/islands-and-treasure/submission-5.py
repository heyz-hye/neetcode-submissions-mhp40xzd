class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q=deque() #deque is a method
        direction=[[1,0],[0,1],[0,-1],[-1,0]]
        dist=0
        visit=set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    q.append([r,c])

        
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                grid[row][col]=dist

                for rw,cl in direction:
                    r=row+rw
                    c=col+cl

                    if r<0 or c<0 or r>=len(grid) or c>=len(grid[0]) or (r,c) in visit or grid[r][c]!=2147483647:
                        continue
                    
                    q.append([r,c])
                    visit.add((r,c))
                
            dist+=1
        