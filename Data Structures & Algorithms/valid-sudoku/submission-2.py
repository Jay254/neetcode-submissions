class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        m, n = len(board), len(board[0])
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)] 
        boxes = [set() for _ in range(9)]

        for r in range(m):
            for c in range(n):
                val = board[r][c]
                if val != '.':
                    box_idx = (r//3)*3 + c//3
                    if val in rows[r] or val in cols[c] or val in boxes[box_idx]:
                        return False
                    rows[r].add(val)
                    cols[c].add(val)
                    boxes[box_idx].add(val)

        return True