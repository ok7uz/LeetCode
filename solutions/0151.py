class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        words.reverse()

        return ' '.join(words)
        


solution = Solution()
print(solution.reverseWords('  hello world  '))     