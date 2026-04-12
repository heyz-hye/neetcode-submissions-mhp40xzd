class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1. Count frequencies
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        
        # 2. Create buckets (index = frequency)
        # We need len(nums) + 1 slots to account for 0 frequency
        freq = [[] for _ in range(len(nums) + 1)]
        
        for n, c in count.items():
            freq[c].append(n)
            
        # 3. Collect the top K
        res = []
        for i in range(len(freq) - 1, 0, -1): # Move backwards
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res