class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def traverse(i, j, idx):
            if board[i][j] != word[idx]:
                return False
            if idx == len(word)-1:
                return True

            temp = board[i][j]
            board[i][j] = '#'

            for dr, dc in directions:
                nr, nc = dr+i, dc + j
                if 0 <= nr < r and 0 <= nc < c:
                    if board[nr][nc] != '#' and traverse(nr, nc, idx+1):
                        board[i][j] = temp
                        return True

            board[i][j] = temp
            return False


        r, c = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]
        for i in range(r):
            for j in range(c):
                if board[i][j] == word[0]:
                    if traverse(i,j,0):
                        return True

        return False