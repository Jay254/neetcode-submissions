class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])

        root = TrieNode()
        for word in words:
            node = root
            for char in word:
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_end = True


        def dfs(r,c,node,path):
            if node.is_end:
                results.add(path)
                node.is_end = False

            if r<0 or r>=rows or c<0 or c>=cols or board[r][c] == "#":
                return

            char = board[r][c]
            if not char in node.children:
                return

            temp = board[r][c]
            board[r][c] = "#"

            dfs(r+1,c,node.children[char], path + char)
            dfs(r-1,c,node.children[char],path + char)
            dfs(r, c+1,node.children[char],path + char)
            dfs(r, c-1, node.children[char],path + char)

            board[r][c] = temp




        results = set()
        for r in range(rows):
            for c in range(cols):
                dfs(r,c,root,"")

        return list(results)
        