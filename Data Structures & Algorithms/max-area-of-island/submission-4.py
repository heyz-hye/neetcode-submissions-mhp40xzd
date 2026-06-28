'''
very similar problem to yesterday

mistakes:
this version uses integer for for element instead of string as suppose last question
The Floating Addition Line: " python dfs(row+1,col)+dfs(row-1,col) +dfs(row,col+1)+
dfs(row,col-1)
In Python, you are calculating the sum
The count += 1 Tracking Bug:
Because you pass count as an argument down into the recursive calls (dfs (row+1, col, count)), 
each call gets its own copy of that integer. When a deeper recursive call increments its own count, 
the parent function call never sees that update.


'''
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[str]]) -> int:
        max_area = 0
        rows, cols = len(grid), len(grid[0])
        
        def dfs(row, col) -> int:
            # Base case: Out of bounds or water ("0")
            if row < 0 or col < 0 or row >= rows or col >= cols or grid[row][col] == 0:
                return 0
            
            # Mark the current cell as visited by sinking it
            grid[row][col] = 0
            
            # Count this cell (1) and add the areas from all 4 directions
            return (1 + 
                    dfs(row + 1, col) + 
                    dfs(row - 1, col) + 
                    dfs(row, col + 1) + 
                    dfs(row, col - 1))

        # Traverse every cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:            
                    # Update max_area if this island is larger
                    max_area = max(max_area, dfs(r, c))
                    
        return max_area
