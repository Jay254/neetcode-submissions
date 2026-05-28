class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # if len(hand) % groupSize != 0:
        #     return False
        
        # count = Counter(hand)
        
        # for num in sorted(count):
        #     while count[num] > 0:  # Try to build as many groups as possible
        #         freq = count[num]
        #         for i in range(groupSize):
        #             next_card = num + i
        #             if count[next_card] < freq:
        #                 return False
        #             count[next_card] -= 1  # Only remove 1 group at a time
        # return True

        #NEETCODE
        if len(hand) % groupSize:
            return False

        count = {}
        for num in hand:
            count[num] = 1 + count.get(num,0)

        minHeap = list(count.keys())
        heapq.heapify(minHeap)

        while minHeap:
            first = minHeap[0]

            for i in range(first, first+groupSize):
                if i not in count:
                    return False
                count[i] -= 1
                if count[i] == 0:
                    if i != minHeap[0]:
                        return False
                    heapq.heappop(minHeap)


        return True
