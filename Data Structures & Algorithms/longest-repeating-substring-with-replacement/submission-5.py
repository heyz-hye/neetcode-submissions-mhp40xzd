'''
Problem: you want to find the longest substrting length that have the same character you can make one to k replacement to make the characters
the same. 
Solution: we will use a hash table and a sliding window technique, we have left and right pointer. Left pointer is set to zero and right
pointer is set to r. left and right record the window length which tell out the answer we want. When we go through the string
we map each letter to the hashtable and map it in letter:number of occurence for that letter. While we increment r we want to see if our window
minus the max occurence of the letter in that window is less than equal to k. If it is, then we need to decrease the count of our current letter 
at left pointer index while increment left pointer by one. This make sure that we stay with k amount of replacement. Then we calculate the max
length of each valid new window with the current window. We return the max length of each valid window.
Note: The hashtable record the occurence of our current window and not of the entire string so whenever our windows change our hashtable values
also changes, therefore if you increment or decrement right and left you need to incremenet or decrement the value of the hashtable for the
corresponding letter at that left or right index
'''
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l=0
        table={}
        maxlength=0
        maxf=0
        
        for r in range(len(s)):
            table[s[r]]=1+table.get(s[r],0)
            maxf=max(maxf,table[s[r]])

            while (r-l+1)-maxf > k:
                table[s[l]]-=1
                l+=1
            maxlength=max(maxlength,r-l+1)
        return maxlength

        