# @leet imports start
# @leet imports end

# @leet start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = "" 
        for i in range(len(s)):
            for j in range(i, (len(s)-i)//2):
                if self.isPalindrome(s,i,j):
                    if j-i > len(max):
                        max = s[i:j]
        return max   
                        
    def isPalindrome(self, s, i, j):
        string = s[i:j]
        return string[::-1] == string


solution = Solution()
print(solution.longestPalindrome("babad"))

        
# @leet end
