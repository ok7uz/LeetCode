List = list


class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        count = tickets[k]
        seconds = 0

        for i in range(count - 1):
            seconds += len(tickets) - tickets.count(0)
            tickets = list(map(lambda x: x - 1 if x > 0 else 0, tickets))

        seconds += k + 1 - tickets[:k].count(0)
        return seconds


solution = Solution()
print(solution.timeRequiredToBuy([84, 49, 5, 24, 70, 77, 87, 8], 3))
