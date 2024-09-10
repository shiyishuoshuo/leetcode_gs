# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node: ListNode) -> Optional[ListNode]:
            if not node or not node.next:
                return node

            last = reverse(node.next)
            node.next.next = node
            node.next = None
            return last

        return reverse(head)


        

        
        