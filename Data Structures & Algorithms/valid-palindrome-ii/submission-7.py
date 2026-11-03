'''
In Python, out-of-bounds slicing does not raise an IndexError. Python automatically adjusts the indices to the boundaries of the sequence, 
returning an empty list if the start index is past the end, or capturing up to the final available element. [1, 2] 

left <= right in valid palindrome is redundant because if the string is odd then when you get to the middle you only left with one element
there is one element by itsel is always valid palindrome

you can pass in l and right pointer of the string instead of the whole string to save declaration and space complexity

outter function very important:
if the s[left] not equal to s[right] then you need to check if removing one character make it a valid palindrome
the thing is, you just gotta check if one of the removal is valid, either you remove the element at the left or the element at the right.
that is why you use a or operator
you also just return the result because it checks rest of the string for you, if removing one character isn't enough then it is automatically false
'''
class Solution:
    def validPalindrome(self, s: str) -> bool:
        left=0
        right=len(s)-1
        def valid(l,r):
            while l<r:
                if s[l]==s[r]:
                    l+=1
                    r-=1
                else:
                    return False
            return True

        
        while left<right: # if one character dont match we go call valid function else we test the string left and right pointer format and see if they are equal

            if s[right]!=s[left]:
                return valid(left+1,right) or valid(left,right-1)
            
            else:
                left+=1
                right-=1
        return True
            
        

        