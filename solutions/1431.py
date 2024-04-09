List = list


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        bool_candies = []

        for candy in candies:
            bool_candies.append(candy + extraCandies >= max_candies)

        return bool_candies
    

solution = Solution()
print(solution.kidsWithCandies([2, 3, 5, 1, 3], 3))
