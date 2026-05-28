class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # found = [False] * 3

        # for triplet in triplets:
        #     if any(triplet[i] > target[i] for i in range(3)):
        #         continue

        #     for i, v in enumerate(triplet):
        #         if v == target[i]:
        #             found[i] = True

        # return all(found)

        good = set()
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue

            for i, v in enumerate(triplet):
                if v == target[i]:
                    good.add(i)

        return len(good) == 3