'''
find the rotten fruit then start a bfs traversal from there similar to island problem
mistake:
misread the problem statement return the time it take for all fresh fruit to be rotted if that state is impossible then return -1

second cleaner solution
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        q=deque()
        fresh=0

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    q.append([r,c])
                if grid[r][c]==1:
                    fresh+=1
        
        while q and fresh>0:
            for i in range(len(q)):
                row,col=q.popleft()
            

                direction=[[1,0],[-1,0],[0,1],[0,-1]]

                for i in range(len(direction)):
                    rw=row+direction[i][0]
                    cl=col+direction[i][1]
                    if rw<0 or cl<0 or rw>=len(grid) or cl>=len(grid[0]) or grid[rw][cl]!=1 :
                        continue
                    else:
                        grid[rw][cl]=2
                        fresh-=1
                        q.append([rw,cl])
            
            time+=1
        if fresh==0:
            return time
        else:
            return -1 
        


        