class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.ans=0
        def dfs(row,col)->bool:
            if row<0 or col<0 or row>=len(grid) or col>=len(grid[0]) or grid[row][col]=="0":
                return False

            grid[row][col]="0"

            res=dfs(row+1,col) or dfs(row-1,col) or dfs(row,col+1) or dfs(row,col-1)

            return res

           

        for r in range(len(grid)):

            for c in range(len(grid[0])):

                if grid[r][c]=="1":

                    self.ans+=1

                    dfs(r,c)

        return self.ans 

        