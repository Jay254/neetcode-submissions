class WordDictionary:

    def __init__(self):
        self.dic = {}

    def addWord(self, word: str) -> None:
        cur = self.dic
        for ch in word:
            if not ch in cur:
                cur[ch] = {}
            cur = cur[ch]
            
        cur['#'] = None

    def search(self, word: str) -> bool:
        def dfs(idx, cur):
            if idx == len(word):
                return '#' in cur

            ch = word[idx]
            if ch == '.':
                for c in cur:
                    if c != '#' and dfs(idx+1, cur[c]):
                        return True
                return False
            if ch not in cur:
                return False

            return dfs(idx+1, cur[ch])

        return dfs(0, self.dic)