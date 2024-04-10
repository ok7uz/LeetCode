from numpy import average


List = list


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_average = last_average = sum(nums[:k]) / k

        for i in range(1, len(nums) - k + 1):
            previous = nums[i - 1]
            last = nums[i + k - 1] if i + k - 1 < len(nums) else 0
            average = (last_average * k - previous + last) / k
            last_average = average
            max_average = max(max_average, average)

        return max_average


solution = Solution()
print(solution.findMaxAverage([0, 1, 1, 3, 3], 4))
