class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        collected = defaultdict(int)
        
        for bill in bills:
            if bill == 5:
                collected[bill] += 1

            elif bill == 10:
                if collected[5] == 0:
                    return False

                collected[5] -= 1
                collected[10] += 1

            else: #bill 20
                if collected[10] > 0 and collected[5] > 0:
                    collected[10] -= 1
                    collected[5] -= 1
                elif collected[5] > 2:
                    collected[5] -= 3
                else:
                    return False
        

        return True