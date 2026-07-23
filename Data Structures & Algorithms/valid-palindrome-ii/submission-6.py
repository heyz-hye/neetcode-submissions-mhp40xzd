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
        l=0
        r=len(s)-1
        def valid(left,right)->bool:
            while left<right:
                while left<right and not s[left].isalnum():
                    left+=1

                while left<right and not s[right].isalnum():
                    right-=1
                
                if s[left].lower()!=s[right].lower():
                    return False
                left+=1
                right-=1
            return True
        
        while l<=r:
            if s[l]!=s[r]:
                return valid(l+1,r) or valid(l,r-1)
            l+=1
            r-=1

        return True

        