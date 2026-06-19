'''
Recursive Permutations Algorithm Logic

• Base Case: Returns a list containing an empty list (`[[]]`). This is crucial so that the `for p in perms:` loop executes at least once when the base case returns.

• Insertion Logic: When the recursive call returns, the goal is to insert the current number at every possible position (front, middle, and back) of each returned permutation list.

• Iteration: We iterate `len(p) + 1` times to account for all these possible insertion slots.

• Copying: A `.copy()` of the returned list (`p`) is made during every single iteration to avoid mutating the original list while building new ones.

• Appending: In every copy, we insert the current number at index `i` (ranging from `0` to `len(p)`) and append this new permutation to our `res` list to return to the next level up.

-Lastly the reason why we did Len(p) +1 is because we can always append the the starting index and the indexes before the last index of the list but to append at last index we must go len(p) +1
'''

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms=[[]]
        for n in nums:
            perm=[]
            for p in perms: #perm is a temporary list that store our incomplete array list
                            #array it need to be reset for every n
                for i in range(len(p)+1):
                    pcopy=p.copy()
                    pcopy.insert(i,n)
                    perm.append(pcopy)
            perms=perm
        return perms




        