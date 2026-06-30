'''
find the rotten fruit then start a bfs traversal from there similar to island problem
mistake:
misread the problem statement return the time it take for all fresh fruit to be rotted if that state is impossible then return -1

how i approach this:
my approach is very similar to the island and treasure, i start from the treasure, in this case the rotted and explore the time it take
for all reachable fresh fruit to become rotted. During the process of exploring every fresh fruit i encounter i set it to rotten which is 2
and after I went through the entire while loop, i check if there is any remaining fresh fruit leftover, if there is that means that fruit is 
unreachable then I return -1. if there isnt a 1 in the matrix, then i return max of 0 and time-1. Zero because there might actually exist
an matrix that have no fresh fruit to begin with. time-1 is because after all the fresh fruit have been explored
the while loop increment by an extra 1 before ending to prepare for the next level, but since there isn't a next level/time it we need to 
decrement it. So max of both is to prevent we returning an -1 by mistake if the actual time is zero
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


        