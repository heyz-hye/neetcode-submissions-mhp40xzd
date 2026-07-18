class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        for i in range(len(stones)):
            stones[i]=-stones[i]
        heapq.heapify(stones)

        while len(stones)>1:
            x=heapq.heappop(stones)
            y=heapq.heappop(stones)

            if abs(y)>abs(x):
                new=abs(y)-abs(x)
                heapq.heappush(stones,-new)
            elif abs(x)>abs(y):
                new=abs(x)-abs(y)
                heapq.heappush(stones,-new)
            else:
                continue
        if len(stones)==0:
            return 0
        else:
            return -heapq.heappop(stones)
                



        
        