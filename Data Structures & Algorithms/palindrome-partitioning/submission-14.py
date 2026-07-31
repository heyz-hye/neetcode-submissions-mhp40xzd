'''
In this problem we first need to separate our task, the first helper function is going to explore what substring there are to group
and the helper fucntion is to tell which substring are valid palindrome.

we use a for loop in the first helper function going from i to the len of s. The reason why we use i is because once we finish the first iteration
starting at the i index we are going to expand our substring from i to j to get every combinations avaliable. If a substring is a valid palindrome
we are going to call the first helper function on the next index after the index j. if it isnt a palindrome we skip it
Every index called can only look ahead and not behind
so index at 1 can only slicing between 1 to the end of the string.
when we reach index out of bound we are going to append a copy of the subset that contains the valid palindromes. when we return we need
to pop to backtrack, every instance of the for loop clean itself after finding all the possible palindromes for that branch.
then after we return if the index i we start with is less than len(s) in the for loop we are going to expand our slicing from i:j
to i:j+1 then we check if that slice is valid palindrome and teh remaining index if it is valid palindrome.
run time is 2^n times n for 2^n combinations and n for palindrome checking and copying,
space complexity is O(n) depth of search which is the len of the string

Note: I was confuse when i trace the code because I realize that there is no return function at the end of for loop for dfs:
Even if a function doesn't have an explicit return statement, 
it will always return control back to the function that called it once it finishes executing its last line of code.
'''

class Solution:
    def validpalindrome(self,s):
        l=0
        r=len(s)-1
        while l<r:
            while l<r and not s[l].isalnum():
                l+=1
            while l<r and not s[r].isalnum():
                r-=1

            if s[l].lower()!=s[r].lower():
                return False
            l+=1
            r-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        res=[]
        part=[]

        def dfs(i):
            if i>=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.validpalindrome(s[i:j+1]):
                    part.append(s[i:j+1])
                    dfs(j+1) #you only pop when you append not what you didn't append that is hwo backtracking work, subset.append,dfs(i+1), subset.pop() dfs(i+1) advance
                    part.pop()
            return
        dfs(0)
        return res
                    




       
          
        