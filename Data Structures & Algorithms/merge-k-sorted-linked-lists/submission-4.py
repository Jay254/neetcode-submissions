# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #put all of them in a heap
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap,(l.val, i, l))
        #now pop from the list and put the values back in a new list
        head = ListNode()
        cur = head
        while heap:
            val, i, l = heapq.heappop(heap)
            cur.next = ListNode(val)
            if l.next:
                heapq.heappush(heap,(l.next.val, i, l.next))
            cur = cur.next

        return head.next