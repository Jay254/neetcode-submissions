class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #something that starts with first letter of our word, say cat
        #something that has same length, = 3
        ch = word[0]
        n = len(word)
        m, n = len(board), len(board[0])
        directions = [(1,0),(0,1),(-1,0),(0,-1)]

        def dfs(i,j,idx):
            if idx == len(word):
                return True

            if i < 0 or i >= m or j < 0 or j >= n:
                return False

            if board[i][j] != word[idx]:
                return False

            temp = board[i][j]
            board[i][j] = '#'

            for dx, dy in directions:
                if dfs(dx+i, dy+j, idx+1):
                    return True

            board[i][j] = temp
            return False


        for i in range(m):
            for j in range(n):
                if board[i][j] == ch:
                    if dfs(i,j,0):
                        return True

        return False