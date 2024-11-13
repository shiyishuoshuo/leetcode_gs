class MonotonicQueue:
        def __init__(self):
            self.max_q = deque([])
            self.min_q = deque([])
        
        def push(self, num:int) -> None:
            while self.max_q and num > self.max_q[-1]:
                self.max_q.pop()
            self.max_q.append(num)

            while self.min_q and num < self.min_q[-1]:
                self.min_q.pop()
            self.min_q.append(num)
        
        def max(self) -> int:
            return self.max_q[0]

        def min(self) -> int:
            return self.min_q[0]
        
        def pop(self, num:int) -> None:
            if self.max_q and num == self.max_q[0]:
                self.max_q.popleft()
            if self.min_q and num == self.min_q[0]:
                self.min_q.popleft()
class Solution:

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        num_len, res = len(nums), -1
        left, right = 0, 0
        window = MonotonicQueue()
        window_size = 0

        while right < num_len:
            window.push(nums[right])
            right += 1

            while left < right and window.max() - window.min() > limit:
                c = nums[left]
                window.pop(c)
                left += 1

            res = max(res, right - left)
        
        return res
        