class Solution:
    def solve(self, board: List[List[str]]) -> None:
        #find entry points in the boundary
        #mark them as something else, say #
        #then find all O's and mark them as x
        
        m, n = len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        #dfs on boundary rows
        def dfs(r,c):
            board[r][c] = '#'
            for dx, dy in directions:
                nx, ny = dx + r, dy + c
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O':
                    dfs(nx, ny)

        #rows
        for i in range(m):
            if board[i][0] == 'O':
                dfs(i,0)
            if board[i][n-1] == 'O':
                dfs(i,n-1)

        #cols
        for j in range(n):
            if board[0][j] == 'O':
                dfs(0,j)
            if board[m-1][j] == 'O':
                dfs(m-1,j)

        #now here set all other points within them as X's
        for r in range(1, m-1):
            for c in range(1, n-1):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        #return all of them marked as '#' back to O's
        for i in range(m):
            for j in range(n):
                if board[i][j] == '#':
                    board[i][j] = 'O'