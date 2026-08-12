'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        target = sorted(s1)
        for i in range(n2 - n1 + 1):
            if sorted(s2[i:i+n1]) == target:
                return True
        return False
'''
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1=len(s1) #you can compare if two hashtbale is equal or not
        n2=len(s2)
        table1=defaultdict(int)
        table2=defaultdict(int)

        if n1>n2:
            return False
        for i in range(n1):
            table1[s1[i]]+=1
            table2[s2[i]]+=1
        
        if table1==table2:
            return True
        
        l=0 #if start l at the wrong index if remove l first then you will run into trouble as you are removing an key that doesn't in the table yet
        r=n1

        while r<n2:
            table2[s2[r]]+=1
            table2[s2[l]]-=1
            if table2[s2[l]]==0:
                del table2[s2[l]]
            
            if table2==table1:
                return True
            
            else:
                l+=1
                r+=1
        
        return False
            




            
