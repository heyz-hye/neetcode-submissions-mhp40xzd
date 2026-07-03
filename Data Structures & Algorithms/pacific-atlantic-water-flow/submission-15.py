'''
I was stuck on this problem for a while, i think it is a really challenging one since there so much details going into it.
So the problem can be divided into two subproblems check whether the water goes to the pacific or atlantic.
naive approach:
visit from every single cell and use dfs or bfs traversal
my original solution i divide the search into two part atlantic and pacific
the two function will pass true if it an index can reach that position, for the res to append, both function need to be true
this solution is very slow as it require combinatoric time of mxn

seeding from border approach:
for bfs and dfs
combine both search into one and use two visit set() and compare the visit set() to find the common index to append to res
tricky part is understanding the reverse gravity. if a index is on the border it is automatically going to flow into its closest ocean
then to explore every index that can get to it, you need the previous index value to be less than the current one.

time complexity:
O(mxn) since visit set avoid the recheck the same index
space complexity:
O(mxn) for the visit set and same run time for the recursion stack for dfs.
however we prefer the bfs over dfs since bfs is iterative and dfs have a call stack which can in reality be surpass python recursion limit
given a grid large enough

mistakes:
on bfs i still call the function every time i append a index
confusing the visit set logic with prev>cur.val, two logic here isnt the same, we append to the visit set only it is a valid index
that can flow to the border
also just because pacific ocean is outbound of bound top and left that doesn't mean you can move in only two directions,
you can move in four direction to have a right path to that ocean

'''


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