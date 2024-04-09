from math import gcd


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1 = len(str1)
        len2 = len(str2)
        len_gcd = gcd(len1, len2)
        common_string = str1[:len_gcd]

        if str1.count(common_string) == len1 // len_gcd and str2.count(common_string) == len2// len_gcd:
            return common_string
        
        return ''
    

solution = Solution()
print(solution.gcdOfStrings('ABABAB', 'ABAB'))
