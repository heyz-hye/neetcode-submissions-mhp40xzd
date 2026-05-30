class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        table=set()
        maxlength=0

        for i in range(len(s)):
            while s[i] in table:
                table.remove(s[l])
                l+=1
            table.add(s[i])
            maxlength=max(maxlength,i-l+1)
        return maxlength

        