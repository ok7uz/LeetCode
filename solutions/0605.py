List = list


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        places = 0
        flowerbed = [0] + flowerbed + [0]

        for i in range(1, len(flowerbed) - 1):
            if flowerbed[i] == flowerbed[i - 1] == flowerbed[i + 1] == 0:
                flowerbed[i] = 1
                places += 1

            if places >= n:
                return True
        
        return False


solution = Solution()
print(solution.canPlaceFlowers([1, 0, 0, 0, 1], 1))
