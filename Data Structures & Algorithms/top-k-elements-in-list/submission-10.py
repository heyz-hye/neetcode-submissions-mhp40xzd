class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        minheap=[]
    
        for val,freq in count.items():
            heapq.heappush(minheap,(freq,val))
        
        while len(minheap)>k:
            heapq.heappop(minheap)
        
        return [heapq.heappop(minheap)[1] for i in range(k)]
            
        