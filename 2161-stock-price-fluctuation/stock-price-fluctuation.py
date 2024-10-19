class StockPrice:

    def __init__(self):
        self.timestampToPrice = {}
        self.latest_timestamp = 0
        self.max_heap = []
        self.min_heap = []

    def update(self, timestamp: int, price: int) -> None:
        self.timestampToPrice[timestamp] = price
        self.latest_timestamp = max(self.latest_timestamp, timestamp)
        heapq.heappush(self.max_heap, (-price, timestamp))
        heapq.heappush(self.min_heap, (price, timestamp))

    def current(self) -> int:
        return self.timestampToPrice[self.latest_timestamp]

    def maximum(self) -> int:
        price, timestamp = self.max_heap[0]
        while -price != self.timestampToPrice[timestamp]:
            heapq.heappop(self.max_heap)
            price, timestamp = self.max_heap[0]

        return -price

    def minimum(self) -> int:
        price, timestamp = self.min_heap[0]
        while price != self.timestampToPrice[timestamp]:
            heapq.heappop(self.min_heap)
            price, timestamp = self.min_heap[0]

        return price


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()
