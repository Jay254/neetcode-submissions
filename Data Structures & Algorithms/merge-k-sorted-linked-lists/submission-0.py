# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0:
            return None

        min_heap = []

        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(min_heap,(lists[i].val,i,lists[i]))

        dummy = ListNode()
        cur = dummy

        while min_heap:
            val, list_idx, node = heapq.heappop(min_heap)

            cur.next = node
            cur = cur.next

            if node.next:
                heapq.heappush(min_heap,(node.next.val,list_idx,node.next))

        return dummy.next
