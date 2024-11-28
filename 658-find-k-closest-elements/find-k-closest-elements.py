class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)

        def left_bound(arr: List[int], target:int) -> int:
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (right - left) // 2 + left
                if arr[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        p = left_bound(arr, x)
        left, right = p - 1, p
        res = deque([])

        while right - left - 1 < k:
            if left == -1:
                res.append(arr[right])
                right += 1
            elif right == n:
                res.appendleft(arr[left])
                left -= 1
            elif arr[right] - x < x - arr[left]:
                res.append(arr[right])
                right += 1
            else:
                res.appendleft(arr[left])
                left -= 1
        return list(res)
        