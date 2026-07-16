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
if the len of the nums greater than k we just pop the heap till it is exactly size k
if the function add append a new value, we push to the heap and it takes O(logn) because it have to traverse up the height of the tree
if after we add the val to the heap then we have more than k element we will pop it until it is size k then we will return nums[0], since
the root always contain the minimum val of the minheap. additonal note popping also heapify things so if you remove an element
it gets turn into a heap and that also take the same run time of heappush

time complexity:
heapify at initialized take O(N)
popping at initialize takes at worst n-k(logn) the time cost at initialize is payed once 
not every single add function call in the previous approach

every push function will take (logk) there is atmost k elements to traverse in the heap to push
every add function will take log(k) because there is atmost one to push and one to pop each time add function call
so depending on how many add function call it is (mlog(k))
overall it is m(logk)

space complexity:
k amount of values so O(K)



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
        
