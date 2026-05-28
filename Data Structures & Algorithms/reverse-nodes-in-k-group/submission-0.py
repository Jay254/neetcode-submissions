# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def getKthNode(node, k):
    count = 0
    while node and count < k-1:
        node = node.next
        count += 1

    return node

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k == 1:
            return head

        dummy = ListNode()
        dummy.next = head

        prevGroupEnd = dummy
        cur = head

        while True:
            kthNode = getKthNode(cur,k)
            if not kthNode:
                break

            nextGrpStart = kthNode.next

            #reverse
            prev = None
            node = cur
            while node != nextGrpStart:
                temp = node.next
                node.next = prev
                prev = node
                node = temp

            prevGroupEnd.next = kthNode
            cur.next = nextGrpStart

            prevGroupEnd = cur
            cur = nextGrpStart

        return dummy.next