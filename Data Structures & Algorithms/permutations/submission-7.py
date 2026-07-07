class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        perms=[[]]
        for n in nums:
            perm=[]
            for p in perms: #perm is a temporary list that store our incomplete array list
                            #array it need to be reset for every n
                            #if you dont reset perm will contain subsets(left over incomplete permutations) of the string because it only modifies and append
                for i in range(len(p)+1):
                    pcopy=p.copy()
                    pcopy.insert(i,n)
                    perm.append(pcopy)
            perms=perm
        return perms




        