class Solution(object):
    def SumSubArr(self, s):
        for i in range(0, len(s)-1):
            left, right = 0, 0
            for j in range(0, i):
                left += s[j]
            for k in range(i, len(s)):
                right += s[k]
            if left == right:
                return True
        return False

sol = Solution()
s = [3, 4, -2, 5, 8, 20, -10, 8]
print(sol.SumSubArr(s))