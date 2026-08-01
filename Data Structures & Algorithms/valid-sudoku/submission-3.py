class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i:set() for i in range(9)}
        cols = {j:set() for j in range(9)}
        boxes = {k: set() for k in range(9)}

        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                k = (i // 3) * 3 + (j // 3)
                if val in rows[i] or val in cols[j] or val in boxes[k]:
                    return False
                rows[i].add(val)
                cols[j].add(val)
                boxes[k].add(val)

        return True