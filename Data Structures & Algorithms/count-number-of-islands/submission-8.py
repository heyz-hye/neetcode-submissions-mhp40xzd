class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island=0
        def dfs(r,c):
            if r<0 or r>=len(grid) or c>=(len(grid[0])) or c<0 or grid[r][c]!="1":
                return
            grid[r][c]="0"

            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)

            return

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c]=="1":
                    island+=1
                    dfs(r,c)
        
        return island
            

        