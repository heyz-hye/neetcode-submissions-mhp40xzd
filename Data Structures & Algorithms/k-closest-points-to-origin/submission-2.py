'''
closest points meaing the smallest distance to the origin so min heap datastructure will be useful here
return k points closest to the origin not only the kth point

my initial approach:
loop through each pair of elements in points calculate the distance, we need to make the
distance negative since we want evict the largest distance greater kth position, we store the negative distance in table so i can reference them
as pair when i want to return them, the format i want to return in is distance as key to pair as values
I also want want to store the key in another array since i can't heapify the table
if length of that heapify table>k we pop till we are at k, then we return the total amount of k element in distance and its corresponding
pair in the table, however this approach has a major flow that it overwrite on collosion, if a pair is different but their distance is the
same, the table[value] will be overwritten by the most recent pair and corrupt the data, also this approach can be optimize in space complexity
in the sense that we dont need the hash table.

optimize approach:
we can store the distance and the coordinates as a tuple, we heapify on the distance and return the k amount of element left in heap
through a for loop and store the coordinates in output array then we return it

To heapify a list of tuples like (0, x, y) based on the integer at the first index (index 0), 
you can pass the list directly into Python's heapq.heapify(). 
Python's heapq module automatically compares tuples by their first element by default

edges case:
if input array is empty return []

times complexity:
the one cost:
loop through the points list takes O(N) and calculate the distance
heapify the distance array also takes O(N)
we do at most t-k(log(n)) pops n stand for the total amout of element in the heap
we store the output through a for loop and that execute at most k times
O(N)+O(N)+t-k(log(N))+O(K)=O(N)

space complexity:
O(N)for the distance array we store tuple in
O(k)also for the output array size
'''
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        table={}
        distance=[]
        output=[]
        
        if not points or not points[0]:
            return []

        for u,v in points:
            val=math.sqrt(u**2+v**2)
            distance.append((val,u,v))
        
        heapq.heapify(distance)

        for i in range(k):
            d=heapq.heappop(distance)
            output.append([d[1],d[2]])
        return output

        
        