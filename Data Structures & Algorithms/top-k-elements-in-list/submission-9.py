class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count=Counter(nums)
        maxheap=[]
        output=[]

        for val,freq in count.items():
            heapq.heappush(maxheap,(freq,val))
        
        while len(maxheap)>k:
            heapq.heappop(maxheap)
        
        for f,v in maxheap:
            output.append(v)

        return output
        