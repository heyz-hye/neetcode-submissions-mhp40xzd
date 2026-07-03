class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res=[]
        if not heights or not heights[0]:
            return res
        rows, cols = len(heights), len(heights[0])
        visitp = set()
        visita = set()

        def dfs(row, col, visit, prevHeight):
            if (
                row < 0 or col < 0 or row == rows or col == cols
                or (row, col) in visit
                or heights[row][col] < prevHeight
            ):
                return
            visit.add((row, col))
            dfs(row + 1, col, visit, heights[row][col])
            dfs(row - 1, col, visit, heights[row][col])
            dfs(row, col + 1, visit, heights[row][col])
            dfs(row, col - 1, visit, heights[row][col])

        for c in range(cols):
            for r in range(rows):
                dfs(0, c, visitp, heights[0][c])
                dfs(rows - 1, c, visita, heights[rows - 1][c])
                dfs(r, 0, visitp, heights[r][0])
                dfs(r, cols - 1, visita, heights[r][cols - 1])

        for r in range(rows):
            for c in range(cols):
                if (r,c) in visita and (r,c) in visitp:
                    res.append([r,c])
        return res