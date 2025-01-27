class MyHashMap:

    def __init__(self):
        self.n = 1009  # A prime number for better distribution
        self.buckets = [[] for _ in range(self.n)]

    def put(self, key: int, value: int) -> None:
        index = key % self.n
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                bucket[i][1] = value
                return
        bucket.append([key, value])

    def get(self, key: int) -> int:
        index = key % self.n
        bucket = self.buckets[index]
        for k, v in bucket:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        index = key % self.n
        bucket = self.buckets[index]
        for i in range(len(bucket)):
            if bucket[i][0] == key:
                del bucket[i]
                return
