'''
since first element of row is always greater than the elements of previous row
already sorted


'''


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flat_list = [item for row in matrix for item in row]

        if target in flat_list:
            return True

        else:
            return False

        
        