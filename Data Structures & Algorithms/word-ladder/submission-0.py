class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0

        word_len = len(beginWord)
        patternMap = defaultdict(list)

        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + "*" + word[i+1:]
                patternMap[pattern].append(word)

        queue = deque([(beginWord,1)])
        visited = set([beginWord])

        while queue:
            cur_word, level = queue.popleft()
            for i in range(word_len):
                pattern = cur_word[:i] + "*" + cur_word[i+1:]
                for neighbor in patternMap[pattern]:
                    if neighbor == endWord:
                        return level + 1
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append((neighbor,level+1))

                patternMap[pattern] = []

        return 0

