class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m, n = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def backtrack(r,c, idx):
            if idx == len(word):
                return True

            if not (0 <= r < m and 0 <= c < n) or board[r][c] != word[idx]:
                return False

            ch = board[r][c]
            board[r][c] = '#'

            for dx,dy in directions:
                nx,ny = dx+r,dy+c
                if backtrack(nx,ny,idx+1):
                    board[r][c] = ch
                    return True

            board[r][c] = ch
            return False
            

        for i in range(m):
            for j in range(n):
                if backtrack(i,j,0):
                    return True

        return False