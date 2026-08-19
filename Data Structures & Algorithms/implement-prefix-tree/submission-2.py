class PrefixTree:

    def __init__(self):
        self.dic = {}

    def insert(self, word: str) -> None:
        cur = self.dic
        for ch in word:
            if not ch in cur:
                cur[ch] = {}
            cur = cur[ch]
        cur['#'] = None

    def search(self, word: str) -> bool:
        cur = self.dic
        for ch in word:
            if not ch in cur:
                return False
            cur = cur[ch]
        return '#' in cur

    def startsWith(self, prefix: str) -> bool:
        cur = self.dic
        for ch in prefix:
            if not ch in cur:
                return False
            cur = cur[ch]

        return True
