class PrefixTree:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        dic = self.trie
        for ch in word:
            if ch not in dic:
                dic[ch] = {}
            dic = dic[ch]
        dic['#'] = True

    def search(self, word: str) -> bool:
        dic = self.trie
        for ch in word:
            if ch not in dic:
                return False
            dic = dic[ch]

        return '#' in dic

    def startsWith(self, prefix: str) -> bool:
        dic = self.trie
        for ch in prefix:
            if ch not in dic:
                return False
            dic = dic[ch]
        return True
        