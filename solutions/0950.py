List = list


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        new_deck = [deck.pop(0)]
        
        for num in deck:
            new_deck = [num] + [new_deck[-1]] + new_deck[:-1]
        
        return new_deck
        

solution = Solution()
print(solution.deckRevealedIncreasing([17, 13, 11, 2, 3, 5, 7]))
