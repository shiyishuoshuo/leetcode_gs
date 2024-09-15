class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.size = 0       

    def get(self, index: int) -> int:
        c = self.head
        if index not in range(self.size):
            return -1
        cur = self.head
        for i in range(index + 1):
            cur = cur.next
        return cur.val
             

    def addAtHead(self, val: int) -> None:
        new_node = ListNode(val)
        tmp = self.head.next
        self.head.next = new_node
        new_node.next = tmp
        self.size += 1
        

    def addAtTail(self, val: int) -> None:
        print(f'size: {self.size}')
        cur = self.head
        for i in range(self.size):
            cur = cur.next
        new_node = ListNode(val)
        cur.next = new_node
        self.size += 1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        new_node = ListNode(val)

        cur = self.head
        for i in range(index):
            cur = cur.next
        if cur:
            tmp = cur.next
            cur.next = new_node
            new_node.next = tmp
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        for i in range(index):
            cur = cur.next
        if cur and cur.next:
            tmp = cur.next.next
            cur.next = tmp
            self.size -= 1
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)