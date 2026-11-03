class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        self.table={}
        maxlength=l=0
        
        for i in range(len(s)):
            self.table[s[i]]=1+self.table.get(s[i],0)

            if (i-l+1)-max(self.table.values())>k:
                self.table[s[l]]-=1
                l+=1
            
            maxlength=max(maxlength,i-l+1)

        return maxlength

