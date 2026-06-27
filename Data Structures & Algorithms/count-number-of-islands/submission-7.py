'''
for every index that is 1 we update our answer to 1 then we call the dfs function on it. The dfs function will visit the index and its
four directions, if the index visited is 1 we mark it zero to avoid revisiting again and also by marking it 0 we can ensure the land is
surround by water.
if index is out of bound or we visited water we return

mistakes i made:
i check if the index element is equal to integer instead of character which the problem state
Python evaluates conditions from left to right. Because grid[row][col] == "0" is placed first, 
Python tries to look up that position in the grid before it checks whether row or col are actually valid boundaries.
grid[row][col] == "0" need to be at the end so error out of bound dont occur

run time m time n 
It might look like the DFS adds a lot of extra time, but remember your sinking mechanic:
The moment the DFS visits a piece of land ("1"), it immediately flips it to water ("0").Because it becomes "0", 
no future DFS call or outer loop iteration will ever process that cell again; they will hit the base case and return False instantly.
Therefore, each cell is actively explored by the DFS at most once.Since each cell is visited a constant number of times 
(checking the 4 directions takes O(1) time per cell), 
the total time spent across all recursive calls is bounded by the total number of cells, which is mxn

space complexity is also mxn in the worst case the whole grid is an giant island and you need to have call depth of mxn
'''

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ans=0
        def dfs(row,col):
            if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col]=="0":
                return
            
            grid[row][col]="0"

            dfs(row+1,col) 
            dfs(row-1,col)  
            dfs(row,col+1)  
            dfs(row,col-1)

            
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    self.ans+=1
                    dfs(r,c)
        return self.ans

        