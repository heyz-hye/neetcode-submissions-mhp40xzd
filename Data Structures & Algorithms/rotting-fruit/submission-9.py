'''
find the rotten fruit then start a bfs traversal from there similar to island problem
mistake:
misread the problem statement return the time it take for all fresh fruit to be rotted if that state is impossible then return -1

second cleaner solution:
we abandon visited set() approach
in this solution you keep track of every single fresh fruit you encounter, then for every fresh fruit you are going to explore you make it 2
so you don't have to run the exploration on duplicate(when two rotted fruit share a adjacent fresh fruit)
and your while condition will also keep track of fresh fruit, the function will run as long as fruit fresh is >0 or there is a queue stack. 
There is two condition that break the while loop, the one condition is that queue finish that is no element to popped and explore but there is
still fresh fruit remaining in that case we return -1 or the other case where the fresh fruit is 0 but there is still something inside queue which
is the last already contaminated fruits, in that case we return time.
we don't need to minus one in this case because that last set of rotted fruit in the queue was never explored.

level != time need to contaminate all the fresh fruits
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
                    if rw<0 or cl<0 or rw>=len(grid) or cl>=len(grid[0]) or grid[rw][cl]!=1: #this case combine two cases grid[rw][cl] equal to 0 or 2
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
        


        