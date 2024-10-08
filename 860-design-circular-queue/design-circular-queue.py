class ListNode:
    def __init__(self, val:int):
        self.val = val
        self.next = None

class MyCircularQueue:

    def __init__(self, k: int):
        self.capacity = k
        self.size = 0
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        

    def enQueue(self, value: int) -> bool:
        if self.size == self.capacity:
            return False

        new_node = ListNode(value)
        if self.size == 0:
            self.head, self.tail = new_node, new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
        self.size += 1
        return True
 

    def deQueue(self) -> bool:
        if self.size > 0:
            self.head = self.head.next
            self.size -= 1
            return True
        return False

        

    def Front(self) -> int:
        if self.size > 0:
            return self.head.val
        return -1
        

    def Rear(self) -> int:
        if self.size > 0:
            return self.tail.val
        return -1
        

    def isEmpty(self) -> bool:
        return self.size < 1
        

    def isFull(self) -> bool:
        return self.size == self.capacity
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()