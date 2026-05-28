class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [['.'] * n for _ in range(n)]
        pos_diags = set()
        neg_diags = set()
        cols = set()
        res = []

        def backtrack(r):
            if r == n:
                res.append([''.join(row) for row in board])
                return

            for c in range(n):
                if c in cols or (r-c) in neg_diags or (r+c) in pos_diags:
                    continue
                
                cols.add(c)
                pos_diags.add(r+c)
                neg_diags.add(r-c)
                board[r][c] = 'Q'

                backtrack(r+1)

                board[r][c] = '.'
                cols.remove(c)
                pos_diags.remove(r+c)
                neg_diags.remove(r-c)

        backtrack(0)

        return len(res)