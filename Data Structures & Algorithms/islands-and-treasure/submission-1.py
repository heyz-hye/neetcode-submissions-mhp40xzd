'''

shortest length to the treasure chest

try dfs from the island doesnt work:
It doesn't guarantee the shortest path first: DFS explores as deep as possible down one path before 
backtracking. If a cell is surrounded by multiple treasures, DFS might take a long, winding path from 
Treasure A to reach it, write down a large number, and then later have to overwrite it when it finds a 
shorter path from Treasure B.
there can be multiple treasure chest and dfs only find a path to one
Redundant work (TLE): Because DFS doesn't find the shortest path automatically, 
you would have to constantly re-visit and re-update cells every time you find a shorter route to them. 
This causes your time complexity to skyrocket, 
often leading to a Time Limit Exceeded (TLE) error.

have to use bfs solution 

The fundamental difference is that (5,2) is a tuple (immutable) and [3.2] is a list (mutable), 
which dictates whether they can be stored in a set. 
Python sets require their elements to be hashable (unchangeable), 
meaning you cannot add a list to a set.

You can pass a list into a set(), but only if the inner elements are unchangeable.


'''
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue=deque()
        visited=set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]==0:
                    queue.append([r,c]) #value here is muttable changeable for list, you can also add immutable element to list
                    visited.add((r,c))
 
        
        dist=0

        while queue:
            for i in range(len(queue)):
                row,col=queue.popleft()
                grid[row][col]=dist
                

                direction=[[1,0],[0,1],[-1,0],[0,-1]]
                for i in range(len(direction)):
                    rw=row+direction[i][0]
                    cl=col+direction[i][1]

                    if cl>=0 and rw>=0 and cl<len(grid[0]) and rw<len(grid) and grid[rw][cl]!=-1 and (rw,cl) not in visited:
                        visited.add((rw,cl))         
                        queue.append([rw,cl])
    
            dist+=1



        

        
                


            


        