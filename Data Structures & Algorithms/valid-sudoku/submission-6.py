'''
check column and check row and also the three by three grid

use a nested for loop to go through each element
for each element I see i want to see if it is in one of the rows sets with that index
and I also want to see if it is in one of the column sets
lastly I check if it is in one of the grid


'''
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        columns = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        for r in range(len(board)):
            for c in range(len(board[r])):
                if board[r][c]==".":
                    continue
                index = (r // 3) * 3 + (c // 3)
                if board[r][c] in rows[r]:
                    return False
                if board[r][c] in columns[c]:
                    return False
                if board[r][c] in boxes[index]:
                    return False
                rows[r].add(board[r][c])
                columns[c].add(board[r][c])
                boxes[index].add(board[r][c])
        return True


        