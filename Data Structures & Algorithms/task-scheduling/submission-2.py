'''
you are given a task schedule:
you want to find the minimum cpu cyles needed to finish the task
identical task need n cooldown time after running

Approach:
1. Count the frequency of each task. Only the frequency matters, not which
   task it is.
2. Put the frequencies into a max-heap (as negatives, since Python's heapq
   is a min-heap). We always want to run the most frequent remaining task
   first — if we don't, we waste time sitting in that task's cooldown
   later, which can't produce the minimum.
3. Use a queue to model the cooldown period (FIFO: whichever task went on
   cooldown first becomes available again first).
   - Each time we pop a task off the heap, we've "used" one instance of it.
     If it still has remaining instances (freq + 1 < 0, since freq is
     negative), we push [freq+1, time+n] onto the queue — the decremented
     count, and the cycle at which it's allowed back in the heap.
4. Loop while either the heap or the queue is non-empty — there's still
   work to do if a task is waiting to run (heap) or waiting on cooldown
   (queue).
5. Increment time at the START of each loop iteration, before touching the
   heap or queue. If we incremented at the end instead, time+n would be
   computed one cycle too early, and the task would become available for
   reuse before its cooldown is actually over.
6. Only push a freq back onto the queue if it's still negative (i.e. some
   count remains). Pushing a freq of 0 would corrupt the heap with a
   "finished" task that has no more instances left.

Worked example (n = 1):
Suppose 3 A's remain, and we're about to pop one at time = 1 (already
incremented this cycle).
  freq going in: -3 -> after pop, fq+1 = -2 (2 A's still remain)
  push [-2, time+n] = [-2, 2] onto the queue
  This means: A can't return to the heap until time reaches 2.

If time had been incremented AFTER the heap/queue logic instead of before,
we'd compute [-2, 1] instead of [-2, 2] — releasing A one cycle too early
and undercounting the true minimum.


notes:
you can return q.popleft() just like you can return heapq.heappop(x)
time complexity:
O(N) for the maxheap heapify
O(N) You pop the sum of frequencies times

mistakes:
1.
if q and q[0][1]==time:
                f=q.popleft()
                heapq.heappush(maxheap,f[0][0])
q.popleft() already give you the item, i am indexing more than it needs(overindexing)
just do f[0]

2.
fq=heapq.heappop(maxheap)
                if fq>0:
                    q.append([fq+1,time+n])

fq is never greater than 0 since we are using maxheap, the frequencies are all negative, condition never reach
what is more is that I am not checking the fq+1 since you want to compare the freq after it has being decremented
if you are not comparing fq+1 you might append an extra freq of 0 into the queue and thus corrupt the data and
elongate the actual minimual amount of time needed

space complexity:
O(N) for the maxheap

'''
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        maxheap=[]
        q=deque()
        time=0

        count=Counter(tasks)

        for val,freq in count.items():
            maxheap.append(-freq)
        
        heapq.heapify(maxheap)

        while maxheap or q:
            time+=1
            if maxheap:
                fq=heapq.heappop(maxheap)
                if fq+1<0:
                    q.append([fq+1,time+n])
            
            if q and q[0][1]==time:
                f=q.popleft()
                heapq.heappush(maxheap,f[0])
        return time



        