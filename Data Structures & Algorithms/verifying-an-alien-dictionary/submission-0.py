class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        word_i = {}
        for idx,ch in enumerate(order):
            word_i[ch] = idx


        for w in range(1, len(words)):
            prev_word, cur_word = words[w-1], words[w]

            c = 0
            shortest = min(len(prev_word), len(cur_word))
            while c < shortest:
                ch1, ch2 = prev_word[c], cur_word[c]
                if word_i[ch1] < word_i[ch2]:
                    break
                elif word_i[ch1] > word_i[ch2]:
                    return False
                c += 1

            if c == shortest and len(prev_word) > len(cur_word):
                return False

        return True