# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

import heapq
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        for listi in lists:
            while listi:
                val = listi.val
                heap.append(val)
                listi = listi.next

        heapq.heapify(heap)
        # print(heap)
        dummy = ListNode()
        cur = dummy
        while heap:
            popped = heapq.heappop(heap)
            # print(popped)
            node = ListNode(popped)
            cur.next = node
            cur = cur.next

        return dummy.next