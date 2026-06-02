'''
return True if there exist a substring in s2 that is a permutation of s1. when you go through all the loop
and haven't find then return false, which mean the permuation does not exist. You need to check first
that the string of s1 is smaller than s2 because if s1 is greater than s2, then no part of s2 will
ever be permutate into s1 because the size doesnt match.

we first compare using the length of s1 for s1 and s2. This initialized our s1 and s2 hash table
with len of s1 amount of letter. If they match initially then we return True.

Then we initialize a left and right pointer that records our window. We initialized 
right pointer to len of s1 index since we already compare s1 length We use a while loop and 
slide the window until r==len(s2). On every iteration we are going to add right pointer element
to our table2. Then we will decrement the frequency of left pointer element, we also check if the left pointer
frequency if it is equal to zero, if it is we just delete the key so in our hash table comparison
we dont need to worry about the extraneous key with frequency of zero. Then we increase our left pointer and 
right pointer by one to fit the window. We also check on 
every iteration if both table 1 and table 2 equal to each other
If r==len(s2) and we break out of the loop then we didnt find any permutation and
return false. The runtime for this should be 26N since there is 26 letters and n elements to go through.
Space compleixty should be O(N) because of the hash table.
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False #there is no way to permutate if the smaller string is larger
        
        table1={} #this is our hashtable for 
        table2={} #

        for i in range(len(s1)):
            table1[s1[i]]=table1.get(s1[i],0)+1
            table2[s2[i]]=table2.get(s2[i],0)+1

        if table1==table2:
            return True
        
        l=0
        r=len(s1)

        while r<len(s2):
            table2[s2[r]]=table2.get(s2[r],0)+1
            table2[s2[l]]-=1

            if table2[s2[l]]==0:
                del table2[s2[l]]
            
            r+=1
            l+=1
            if table1==table2:
                return True
        return False

        