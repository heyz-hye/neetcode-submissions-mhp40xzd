class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base case: stay within bounds and only sink land ('1')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the current cell as visited (sink it)
            grid[r][c] = '0'
            
            # Explore all 4 neighbors
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    island_count += 1
                    dfs(r, c) # Start sinking the discovered island
                    
        return island_count