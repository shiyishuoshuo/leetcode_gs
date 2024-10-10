class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None
        self.prev = None

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = 0
        self.capacity = k
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = ListNode(value)
        if self.isEmpty():
            self.head, self.tail = newNode, newNode
        else:    
            newNode.next = self.head
            self.head.prev = newNode
            self.head = newNode
        self.size += 1
        return True
        
        

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        newNode = ListNode(value)
        if self.isEmpty():
            self.head, self.tail = newNode, newNode
        else:    
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.size += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        newHead = self.head.next
        self.head.next = None
        if newHead:
            newHead.prev = None
        self.head = newHead
        self.size -= 1
        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        preTail = self.tail.prev
        if preTail:
            preTail.next = None
        self.tail.prev = None
        self.tail = preTail
        self.size -= 1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.head.val
        

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.val

    def isEmpty(self) -> bool:
        return self.size < 1
        

    def isFull(self) -> bool:
        return self.capacity == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()