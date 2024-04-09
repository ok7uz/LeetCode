class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_length = min(len(word1), len(word2))
        string = ''

        for i in range(min_length):
            string += word1[i] + word2[i]
        
        string += word1[min_length:] + word2[min_length:]
        return string


solution = Solution()
print(solution.mergeAlternately('abcd', 'pq'))
