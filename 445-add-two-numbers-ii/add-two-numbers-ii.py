# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1, s2 = [], []
        while l1:
            s1.append(l1)
            l1 = l1.next
        while l2:
            s2.append(l2)
            l2 = l2.next
        
        dummy = ListNode(-1)
        carry = 0

        while s1 or s2 or carry:
            value = carry
            if s1:
                value += s1.pop().val
            if s2:
                value += s2.pop().val
            carry, value = divmod(value, 10)
            new_node = ListNode(value)
            tmp = dummy.next
            dummy.next = new_node
            new_node.next = tmp
        return dummy.next



        