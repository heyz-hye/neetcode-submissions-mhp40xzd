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

        