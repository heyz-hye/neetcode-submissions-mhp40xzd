class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        res=[]
        
        if not heights or not heights[0]:
            return res
        
        visitp=set()
        visita=set()
        p=deque()
        a=deque()
        def bfs(queue,visit):
            while queue:
                row,col=queue.popleft()

                direction=[[1,0],[0,1],[-1,0],[0,-1]]
                
                for i in range(len(direction)):
                    rw=row+direction[i][0]
                    cl=col+direction[i][1]
                    if cl<0 or rw<0 or rw==len(heights) or cl==len(heights[0]) or (rw,cl) in visit or heights[row][col]>heights[rw][cl]:
                        continue
                    else:
                        visit.add((rw,cl))
                        queue.append([rw,cl])        

        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if r==0 or c==0:
                    p.append([r,c])
                    visitp.add((r,c))
                    bfs(p,visitp)
                if r==len(heights)-1 or c==len(heights[0])-1:
                    a.append([r,c])
                    visita.add((r,c))
                    bfs(a,visita)
    
        
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in visita and (r,c) in visitp:
                    res.append([r,c])
        return res