class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {ch:i for i,ch in enumerate(order)}

        word_prev = words[0]
        for word_cur in words[1:]:
            word_len = min(len(word_prev), len(word_cur))
            ties = True

            for i in range(word_len):
                ch_prev, ch_cur = word_prev[i], word_cur[i]
                if ch_prev != ch_cur:
                    if dic[ch_prev] > dic[ch_cur]:
                        return False
                    else:
                        ties = False
                        break
            
            if ties and len(word_prev) > len(word_cur):
                return False

            word_prev = word_cur

        return True
