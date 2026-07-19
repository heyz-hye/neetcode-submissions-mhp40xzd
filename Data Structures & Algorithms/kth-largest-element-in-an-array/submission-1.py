'''
there can be duplicate number with the same value that means same number that actually take multiple spots in largest position:
ex:1,4,4,4,4 k=4 output will be 4 


'''
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k>len(nums):
            return 0
        maxheap=[]
        for i in nums:
            heapq.heappush(maxheap,-i)
        
        for i in range(k-1):
            heapq.heappop(maxheap)
        
        return -maxheap[0]
            


        



            

        
        