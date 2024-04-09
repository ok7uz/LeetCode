class Solution:
    vowels = 'aeuioAEUIO'

    def reverseVowels(self, s: str) -> str:
        s_vowels = list(filter(lambda i: i in self.vowels, s))
        s_vowels.reverse()
        s_vowels = iter(s_vowels)
        reverse_s = ''

        for i in s:
            if i in self.vowels:
                reverse_s += next(s_vowels)
            else:
                reverse_s += i

        return reverse_s
    

solution = Solution()
print(solution.reverseVowels('leetcode'))     
