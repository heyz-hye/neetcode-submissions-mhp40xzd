class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        # sorted() returns a list of characters in alphabetical order
        return sorted(s) == sorted(t)