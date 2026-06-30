'''
find the rotten fruit then start a bfs traversal from there similar to island problem
mistake:
misread the problem statement return the time it take for all fresh fruit to be rotted if that state is impossible then return -1
'''
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time=0
        visited=set()
        q=deque()

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==2:
                    visited.add((r,c))
                    q.append([r,c])
        
        while q:
            for i in range(len(q)):
                row,col=q.popleft()
                grid[row][col]=2
            

                direction=[[1,0],[-1,0],[0,1],[0,-1]]

                for i in range(len(direction)):
                    rw=row+direction[i][0]
                    cl=col+direction[i][1]
                    if rw<0 or cl<0 or rw>=len(grid) or cl>=len(grid[0]) or grid[rw][cl]==0 or (rw,cl) in visited:
                        continue
                    else:
                        visited.add((rw,cl))
                        q.append([rw,cl])
            
            time+=1
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==1:
                    return -1
        return max(0,time-1)


        