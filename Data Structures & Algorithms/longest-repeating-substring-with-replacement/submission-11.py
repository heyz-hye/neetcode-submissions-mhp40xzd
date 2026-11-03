class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        self.table={}
        l=0
        maxlength=0
        maxf=0
        for i in range(len(s)):
            self.table[s[i]]=1+self.table.get(s[i],0)
            maxf=max(maxf,self.table[s[i]])

            if (i-l-maxf+1)>k: #your left pointer shift it doesnt anchor at zero, the length you compare isright to left lenght +1
                self.table[s[l]]-=1
                l+=1
                
            maxlength=max(maxlength,i-l+1)

        return maxlength

