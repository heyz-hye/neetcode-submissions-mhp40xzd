class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res=[]
        
        if not heights or not heights[0]:
            return res
        
        visitp=set()
        visita=set()

        def dfs(r,c,visit,prev):

            if r<0 or c<0 or r==len(heights) or c==len(heights[0]) or prev>heights[r][c] or (r,c) in visit:
                return
            
            visit.add((r,c))
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r==0 or c==0:
                    dfs(r,c,visitp,heights[r][c])
                if r==len(heights)-1 or c==len(heights[0])-1:
                    dfs(r,c,visita,heights[r][c])
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in visita and (r,c) in visitp:
                    res.append([r,c])
        return res