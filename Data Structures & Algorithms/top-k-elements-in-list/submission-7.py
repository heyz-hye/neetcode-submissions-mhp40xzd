class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        maxheap=[]

        for val,freq in count.items():
            heapq.heappush(maxheap,(-freq,val))
        
        return [heapq.heappop(maxheap)[1] for i in range(k)]
        