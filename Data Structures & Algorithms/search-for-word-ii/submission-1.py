class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            node = root
            for ch in word:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = word

        m, n = len(board), len(board[0])
        directions = [(1,0),(-1,0),(0,-1),(0,1)]

        def dfs(r,c,node):
            ch = board[r][c]
            if ch not in node.children:
                return 
            
            nxt = node.children[ch]
            if nxt.word:
                res.append(nxt.word)
                nxt.word = None

            board[r][c] = '#'

            for dx, dy in directions:
                nx, ny = dx+r, dy+c
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '#':
                    dfs(nx, ny, nxt)

            board[r][c] = ch

            if not nxt.children:
                node.children.pop(ch)


        res = []
        for r in range(m):
            for c in range(n):
                dfs(r, c, root)

        return res