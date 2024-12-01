# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        cur, nextGroupHead = head, head
        for _ in range(k):
            if not nextGroupHead:
                return head
            nextGroupHead = nextGroupHead.next

        last = self.reverseN(cur, k)
        cur.next = self.reverseKGroup(nextGroupHead, k)
        return last
    
    def reverseN(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 1 -> 2
        if not head or not head.next:
            return head
        pre, cur, nxt = None, head, head.next
        while n > 0:
            cur.next = pre
            pre = cur
            cur = nxt
            if nxt.next:
                nxt = nxt.next
            n -= 1
        head.next = cur
        return pre