class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visit=set()
        safe=set()
        table={}
        self.res=[]

        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in table:
                table[prerequisites[i][0]]=[prerequisites[i][1]]
            else:
                 table[prerequisites[i][0]].append(prerequisites[i][1])
        
        def dfs(prerequisites)->bool:
            if prerequisites in safe:
                return True
            if table.get(prerequisites,[])==[]:
                self.res.append(prerequisites)
                safe.add(prerequisites)
                return True
            if prerequisites in visit:
                return False
            visit.add(prerequisites)
            for i in table[prerequisites]:
                if not dfs(i):
                    return False
            self.res.append(prerequisites)
            visit.remove(prerequisites)
            safe.add(prerequisites)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return []
   
        return self.res
        