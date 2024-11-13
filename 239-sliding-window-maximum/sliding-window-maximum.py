import collections

class MonotonicQueue:
        def __init__(self):
            self.q = deque([])
        
        def push(self, num:int) -> None:
            while self.q and num > self.q[-1]:
                self.q.pop()
            self.q.append(num)
        
        def max(self) -> int:
            return self.q[0]
        
        def pop(self, num:int) -> None:
            if num == self.q[0]:
                self.q.popleft()

class Solution:
    
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = MonotonicQueue()
        res = []

        for i in range(len(nums)):
            if i - k + 1 < 0:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i - k + 1])
        
        return res

        