class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            board[r][c] = 'T'  # Temporarily mark this 'O' to avoid capturing it.
            # Move in all four directions (up, down, left, right).
            dfs(r - 1, c)  # Up
            dfs(r + 1, c)  # Down
            dfs(r, c - 1)  # Left
            dfs(r, c + 1)  # Right

        # Step 1: Mark all 'O's connected to the border.
        # Traverse the first and last row.
        for c in range(cols):
            if board[0][c] == 'O':
                dfs(0, c)  # First row
            if board[rows - 1][c] == 'O':
                dfs(rows - 1, c)  # Last row

        # Traverse the first and last column.
        for r in range(rows):
            if board[r][0] == 'O':
                dfs(r, 0)  # First column
            if board[r][cols - 1] == 'O':
                dfs(r, cols - 1)  # Last column

        # Step 2: Flip all remaining 'O's to 'X', and all 'T's back to 'O'.
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'  # Flip surrounded 'O' to 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'  # Restore border-connected 'O'