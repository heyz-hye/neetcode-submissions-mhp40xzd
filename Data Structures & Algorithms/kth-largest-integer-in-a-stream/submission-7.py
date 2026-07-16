'''
first attemp work for one add not subsetquent add function call
The real problem: in add, you pop t elements off the heap to "get down to" the kth largest, 
then pop once more to return it — 
but you never push those popped elements back. That permanently shrinks self.nums on every call, 
so the heap is corrupted for the next add(). 
You'd also be doing O(k log n) work per call, when this problem has an O(log k) solution.
reason why is because you The loop runs t = n - k times, and each iteration does an O(log n) pop. 
So the total cost is: O((n-k)logn
If k is small compared to n (say k=3 and n=10000), that loop runs ~9997 times — this is essentially O(n log n) per call, not O(log n). 
That's much worse, and it also has the correctness bug we discussed: 
those popped elements never get pushed back, so your heap loses data permanently after the first add() call.

you can do quickselect algorithm but depending on the pivot it can take n-n^2 time
you can do sort the array and do bianry search which take log(N) but combine with every single add, append things to the sorted array take O(N)
for both of these approaches depend on how many times add it is called, it can take m(n) which is O(n^2)

we choose minheap datastructure to solve this
in our initialized code we can initiate our nums and call heapify on it to make it a heap this takes O(N) base on floyd algorithm
inserting from the middle level of the tree.



'''

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k=k
        heapq.heapify(nums) #this takes O(N)
        self.nums=nums
        while len(self.nums)>k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums,val)
        
        if len(self.nums)>self.k:
            heapq.heappop(self.nums)
        return self.nums[0]
        
