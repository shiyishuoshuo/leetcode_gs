class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        q = deque()
        times = 0
        # so that this queue needs to save (index, tickets[index])

        for index, ticket in enumerate(tickets):
            q.append((index, ticket))

        while q:
            index, ticket = q[0]
            if index == k and ticket == 1:
                return times + 1
            q.popleft()
            if ticket > 1:
                q.append((index, ticket - 1))
            times += 1

        return times
        