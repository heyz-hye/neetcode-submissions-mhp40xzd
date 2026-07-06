class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit=set()
        safe=set()
        table={}
        self.res=True

        for i in range(len(prerequisites)):
            if prerequisites[i][0] not in table:
                table[prerequisites[i][0]]=[prerequisites[i][1]]
            else:
                 table[prerequisites[i][0]].append(prerequisites[i][1])
        
        def dfs(prerequisites)->bool:
            if prerequisites in safe:
                return True
            if table.get(prerequisites,[])==[]:
                return True
            if prerequisites in visit:
                return False
            visit.add(prerequisites)
            for i in table[prerequisites]:
                self.res=self.res&dfs(i)
            visit.remove(prerequisites)
            return self.res
        
        for i in range(len(prerequisites)):
            if not dfs(prerequisites[i][0]):
                return False
            else:
                safe.add(prerequisites[i][0])     
        return True






        



        