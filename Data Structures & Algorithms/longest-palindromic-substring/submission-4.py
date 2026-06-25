'''
brute force approach:
you use does for loop and check every single substring variation and check if those substring are palindrome at the same time this
takes O(N)^3 time

improve solution: using a for loop we can check each index and expand outward if the right and left pointer matches we compare the result
length with distance between right and left pointer +1 and if the new substring length is greater we make that our new result len and make that
substring our result. If the right and left pointer isnt the same we just break out of the while loop.

Edge case for even length string: we need to make left pointer i and right pointer i+1
for odd length make both pointer start from the same index.

Run time O(N)^2
space complexity O(1)

'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res=""
        reslen=0

        for i in range(len(s)):
            l=i
            r=i
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    if r-l+1>reslen:
                        res=s[l:r+1]
                        reslen=r-l+1
                    l-=1
                    r+=1
                else:
                    break
            l=i
            r=i+1
            while l>=0 and r<len(s):
                if s[l]==s[r]:
                    if r-l+1>reslen:
                        res=s[l:r+1]
                        reslen=r-l+1
                    l-=1
                    r+=1
                else:
                    break
        return res