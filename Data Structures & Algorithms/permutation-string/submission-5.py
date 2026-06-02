class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False #there is no way to permutate if the smaller string is larger
        
        table1={}
        table2={}

        for i in range(len(s1)):
            table1[s1[i]]=table1.get(s1[i],0)+1
            table2[s2[i]]=table2.get(s2[i],0)+1

        if table1==table2:
            return True
        
        for i in range(len(s1),len(s2)):
            table2[s2[i]]=table2.get(s2[i],0)+1
            left=s2[i-len(s1)]
            table2[left]-=1

            if table2[left]==0:
                del table2[left]
            if table2==table1:
                return True
        return False
        
        
                
            

        