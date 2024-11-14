class MonolicQueue:
    def __init__(self):
        self.q = deque([])

    def push(self, n: int) -> None:
        while self.q and self.q[-1] > n:
            self.q.pop()
        self.q.append(n)

    def min(self) -> int:
        return self.q[0]

    def pop(self, n: int) -> None:
        if self.q and self.q[0] == n:
            self.q.popleft()

    def isEmpty(self) -> bool:
        return not self.q


class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        prefix_sum = [0] * (n + 1)
        for i in range(1, n + 1):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]

        window = MonolicQueue()
        left, right = 0, 0
        res = float("inf")

        while right < len(prefix_sum):
            window.push(prefix_sum[right])
            right += 1

            while (
                left < right
                and right < len(prefix_sum)
                and not window.isEmpty()
                and prefix_sum[right] - window.min() >= k
            ):
                res = min(res, right - left)
                window.pop(prefix_sum[left])
                left += 1

        return -1 if res == float("inf") else res
