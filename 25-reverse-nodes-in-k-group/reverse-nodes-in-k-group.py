# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        cur, nxt = head, head

        cnt = k

        while cnt > 0 and nxt:
          nxt = nxt.next
          cnt -= 1
        
        if cnt > 0:
            return head
        
        new_head = self.reverseN(cur, nxt)
        cur.next = self.reverseKGroup(nxt, k)
        return new_head
    
    def reverseN(self, a: Optional[ListNode], b: Optional[ListNode]):
        if not a or not a.next:
            return a

        pre, cur, nxt = None, a, a
        while cur != b:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt            
        return pre

