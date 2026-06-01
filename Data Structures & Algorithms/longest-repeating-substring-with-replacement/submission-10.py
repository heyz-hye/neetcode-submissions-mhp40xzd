class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        table={}
        l=0
        maxlength=0
        maxf=0

        for i in range(len(s)):
            table[s[i]]=1+table.get(s[i],0)
            maxf=max(maxf,table[s[i]])

            if (i-l+1)-maxf>k:
                table[s[l]]-=1
                l+=1
            maxlength=max(maxlength,i-l+1)
        return maxlength

