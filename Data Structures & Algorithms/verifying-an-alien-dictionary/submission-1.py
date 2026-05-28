class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        lex = {ch:i for i,ch in enumerate(order)}
        n = len(words)
        
        for i in range(1, n):
            w1, w2 = words[i-1], words[i]
            m = min(len(w1), len(w2))
            for j in range(m):
                if lex[w1[j]] < lex[w2[j]]:
                    break
                elif lex[w1[j]] > lex[w2[j]]:
                    return False
            else:
                if len(w1) > len(w2):
                    return False

        return True