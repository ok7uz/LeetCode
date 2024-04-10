class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for i in s:
            if i not in t:
                return False
            
            t = t[t.index(i) + 1:]
        
        return True
        


solution = Solution()
print(solution.isSubsequence('aaaaaa', 'bbaaaaa'))
