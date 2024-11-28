class TimeMap:

    def __init__(self):
        self.map = {} # key will be the key value will be list of [val, timestamp]
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map.get(key).append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        res = ''
        if key not in self.map:
            return res

        if timestamp < self.map[key][0][0]:
            return res
        
        left, right = 0, len(self.map[key]) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if self.map[key][mid][0] <= timestamp:
                left = mid + 1
            else:
                right = mid - 1
        return self.map[key][right][1] if right >= 0 else ""
            
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)