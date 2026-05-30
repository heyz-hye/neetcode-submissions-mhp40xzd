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

common sense version use length of window - max(freq.values()) this cost 26N as table has 26 possible letters

unintuitive version we use length of window -maxf.
maxf explanation: instead of recalculating max(freq.value)() every while loop we can use maxf. maxf compare every letter encounter whiile
going through the string to see if it is max frequency, since it is comparing with atmost one letter on each comparison it is O(1) significantly
more efficient than max(freq.value()). Note maxf isnt the true highest ocurrence of the letter every time, but since we are finding the max length
we can tolerate it since the bigger the window the bigger the maxf it need to be to satisfy the conditon r-l+1-maxf<=k.

but by being lenient on the condition we allow to many windows that shouldnt be counted in the first place?
yes, but if the window is truly invalid that means there is also exist of a subset of it that is valid and as the Left pointer shrink the window
and also as r move we will derive at the accurate valid length eventually

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

        