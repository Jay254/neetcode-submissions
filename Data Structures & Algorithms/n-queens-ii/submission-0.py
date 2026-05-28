class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.'] * n for _ in range(n)]
        res = []
        cols = set()
        pos_diags = set()
        neg_diags = set()

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return
            for c in range(n):#for each cols
                if c in cols or (r+c) in pos_diags or (r-c) in neg_diags:
                    continue
                
                cols.add(c)
                pos_diags.add(r+c)
                neg_diags.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                cols.remove(c)
                pos_diags.remove(r+c)
                neg_diags.remove(r-c)
                board[r][c] = '.'


        backtrack(0)

        return len(res)