class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxheap=[]
        q=deque()
        time=0

        count=Counter(tasks)

        for val,freq in count.items():
            heapq.heappush(maxheap, -freq)

        heapq.heapify(maxheap)

        while maxheap or q:
            time+=1
            if maxheap:
                f=heapq.heappop(maxheap)
                if f+1<0:  #what if this goes to postive we will append postive freq in maxheap?, it doesn't.
                    q.append([f+1,time+n])
            
            if q and q[0][1]==time:
                fq=q.popleft()
                heapq.heappush(maxheap,fq[0])
                    
        return time
        