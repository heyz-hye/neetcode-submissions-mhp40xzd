'''
we must sort the list in order to see the adjacent duplicates within the list
our base case if we find the total equal to target we will append cur which is our subset to our res
we use a for loop to explore every possible option that is less than the target
if it there is a adjacent candidate we will continue to skip that iteration
if there is a future candidate that we want to add to total that will exceed our target we will skip the entire for loop
because the list is sorted the every element after that subsequent element will be greater 
we will recurse to the next index in the list and set that as the beginning of our list
cur.pop()  we delete the element within cur after we explore every single possible iteration of it
'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res=[]
        candidates.sort()
      

        def tree(i,cur,total):
            if total==target:
                self.res.append(list(cur))
                return
            
            for j in range(i,len(candidates)):
                if j>i and candidates[j]==candidates[j-1]:
                    continue
                if total+candidates[j]>target:
                    break
                
                cur.append(candidates[j])
                tree(j+1,cur,total+candidates[j])
                cur.pop()
        tree(0,[],0)

        return self.res

