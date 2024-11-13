import collections
class Solution:
    class monotonicQueue:
        def __init__(self):
            self.dq = deque([])

        def push(self, val:int) -> None:
            while self.dq and val > self.dq[-1]:
                self.dq.pop()
            self.dq.append(val)
        def max(self) -> int:
            return self.dq[0]

        def pop(self, n) -> None:
            if n == self.dq[0]:
                self.dq.popleft()

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = self.monotonicQueue()
        res = []
        for i in range(len(nums)):
            # when i = k - 1 then we form the first window k
            # so the first if clause was to push first k to the queue
            if i < k - 1:
                window.push(nums[i])
            else:
                window.push(nums[i])
                res.append(window.max())
                window.pop(nums[i - k + 1])

        return res

        
        