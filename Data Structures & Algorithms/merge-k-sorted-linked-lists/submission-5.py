# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []

        for i, l in enumerate(lists):
            heapq.heappush(heap, (l.val, i, l))

        dummy = ListNode()
        res = dummy
        while heap:
            val, idx, node = heapq.heappop(heap)
            res.next = ListNode(val)
            if node.next:
                node = node.next
                heapq.heappush(heap, (node.val, idx, node))
            res = res.next

        return dummy.next