'''
since first element of row is always greater than the elements of previous row
already sorted


'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = [item for row in matrix for item in row]

        low=0
        high=len(flat_list)-1

        while low<=high:
            midpoint=(low+high)//2
            if flat_list[midpoint]==target:
                return True
            
            if target<flat_list[midpoint]:
                high=midpoint-1

            if target>flat_list[midpoint]:
                low=midpoint+1

        return False



        
        