'''
you are given a task schedule:
you want to find the minimum cpu cyles needed to finish the task
identical task need n cooldown time after running

approach:
start off with matching each freq and heapify in a maxheap,
the name of the task don't matter but the number of the same task matter
if we dont start off popping the most frequent task then we will waste more
time in the cooldown period of that time. That does not help us find the minimum cpu cycles
then you use queue datastructure to imitate first in first out cooldown wait list
in the queue you will store the freq of the task after it has being pop from
the heap, so you have to first decrement the frequency of task and 
add the time you are on current along with the cooldown time and store it 
as a tuple inside the queue. While there is a queue or maxheap the loop
keep going because there are still task left to pop if maxheap exist, or
task waiting to be push in and then pop for queue datastructure.
We also need to increment the time before the we check for maxheap
and queue operations because if we incremenet time after those maxheap
and queue condition statement we will inaccurately reflect the cooldown of
the task we are suppose to push in. Like we push in the task too early
we only push the freq into the queue only if the frequency is greater than zero,
because if it is equal to zero we are done with the task else the function will
go on forever

For example:
there are three A task
if task A is is done and the cooldown time is 1, currently the time is 0 before we havent
incremented yet, the queue will store [-2,1] and after we increment the time, A become instantly
availiable when it suppose to wait till time 2. the second index of the tuple represent when 
the task can be push back into the heap again.
Every time you pop off heap, that freq is temporarily remove from the heap into the queue.

time complexity:
O(N) for the maxheap heapify
O(N) You pop the sum of frequencies times

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
                heapq.heappush(maxheap,q.popleft()[0])
        return time



        