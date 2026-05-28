class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        dic = self.trie
        for ch in word:
            if not ch in dic:
                dic[ch] = {}
            dic = dic[ch]
        dic['#'] = True

    def search(self, word: str) -> bool:
        def dfs(dic, idx):
            if idx == len(word):
                return '#' in dic

            ch = word[idx]
            if ch != '.': #not wildcard character
                if ch not in dic:
                    return False
                return dfs(dic[ch], idx+1)
            else:
                for l in dic:
                    if l != '#' and dfs(dic[l], idx+1):
                        return True
                return False

        return dfs(self.trie, 0)