class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []

        board = [['.'] * n for _ in range(n)]

        cols = set()
        pos_diagonals = set() #/
        neg_diagonals = set() #\

        def backtrack(row):
            if row == n:
                res.append(["".join(r) for r in board])
                return

            for col in range(n):
                if col in cols or (row+col) in pos_diagonals or (row-col) in neg_diagonals:
                    continue
                
                board[row][col] = 'Q'
                cols.add(col)
                pos_diagonals.add(row+col)
                neg_diagonals.add(row-col)

                #now we backtrack
                backtrack(row+1)

                board[row][col] = '.'
                cols.remove(col)
                pos_diagonals.remove(row+col)
                neg_diagonals.remove(row-col)

        backtrack(0)
        return res





