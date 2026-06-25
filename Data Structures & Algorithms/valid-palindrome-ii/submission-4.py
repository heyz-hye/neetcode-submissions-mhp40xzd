class Solution:
    def validPalindrome(self, s: str) -> bool:
        def valid(s)->bool:
            l = 0
            r = len(s) - 1
            while l < r:
            # Skip non-alphanumeric characters
                while l < r and not s[l].isalnum():
                    l += 1
                while l < r and not s[r].isalnum():
                    r -= 1

            # Perform the actual comparison
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
            return True
        if valid(s):
            return True
        for i in range(len(s)):
            if valid(s[:i] + s[i+1:]):
                return True
        return False

        