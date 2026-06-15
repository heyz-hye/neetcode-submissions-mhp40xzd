'''
can use a dfs approach every time you move see an element you create 2 path from that index, one path contains the element another doesnt contain it.
You keep doing it until you can hit the base case where your i is out of bound. Every call give 2 path since there is n elements
there is 2^n avaliable paths. run time is n times 2 to the N, space complexitiy is is also n times 2 ^n.

Creating a copy of the path list takes time proportional to its current length, which is O(n) in the worst case this is the n in space complexity.
Every row has an average length of n/2. this is  the n in space complexity.

'''
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.ans=[]
        self.subset=[]
        def dfs(i):
            if i>=len(nums):
                self.ans.append(self.subset.copy())
                return
            self.subset.append(nums[i])
            dfs(i+1)
            self.subset.pop()
            dfs(i+1)
        dfs(0)
        return self.ans




        

        