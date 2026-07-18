'''
my approach:
since they are looking for the largest weight stones i want to loop through stones and make them all negative so that the minheap will
return the maxheap answer.
python dont have an existing maxheap function
so making the individual indexes negative will produce a negative version of maxheap, what we gotta do is just turn it postive using absolute
value or negate the negative.

Then for the while loop for len(stones) is greater than 1 we can keep popping two x and y so that we can give the smash the stones
when we smash the stones we take the negative absolute value of their difference and we push in back to the stones heap. we have to make
the remaining stone negative or else it will corrupt the data. if two stones are smash and both are 0 we just skip the loop.

edges case:
if the len of the stones we are given is 0 we return 0
if the len of stoens we are left with is 0 after the while we know that both smash destroy each other in the last step
so we return a zero

we return the last element of the heap as our answer

time complexity:
- marking stones negative: O(n)
- heapify: O(n)
- main loop: runs ~n/2 times, each iteration does up to 2 pops + 1 push,
  each O(log n) -> O(n log n) total
overall: O(n) + O(n) + O(n log n) = O(n log n)

space complexity:
O(n) - heap holds all n elements

mistakes:
 if abs(y)>abs(x):
                new=abs(y)-abs(x)
                heapq.heappush(stones,-new)
elif abs(x)>abs(y):
                new=abs(x)-abs(y)
                heapq.heappush(stones,-new)
since we pop x first that meant it has to be greater than or equal to y it will never be smaller than y, that is how heap work
'''
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

            if abs(x)>abs(y):
                new=abs(x)-abs(y)
                heapq.heappush(stones,-new)
            else:
                continue
        if len(stones)==0:
            return 0
        else:
            return -heapq.heappop(stones)
                



        
        