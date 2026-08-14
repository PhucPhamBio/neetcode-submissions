class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxs = [set() for _ in range(9)]


        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                value = int(board[i][j])
                boxid = (i//3)*3 + j//3
                if  (value in rows[i]) or  (value in cols[j]) or  (value in boxs[boxid]):
                    return False

                rows[i].add(value)
                cols[j].add(value)
                boxs[boxid].add(value)
        return True