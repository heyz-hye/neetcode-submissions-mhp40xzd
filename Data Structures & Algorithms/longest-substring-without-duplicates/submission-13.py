class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        map={}
        max_length=0

        for i in range(len(s)):
            curr=s[i]

            if curr in map and map[curr]>=left: #left pointer should only move forward and not backward
                                                #going by will include duplicates that was already check.
                left=map[curr]+1

            map[curr]=i 

            length=i-left+1
            max_length=max(max_length, length)
                
        return max_length
            