class Solution(object):
    def SumSubArr(self, s):
        maxi = -2**35 -1
        for i in range(len(s)):
            prifix = 0
            for j in range(i, len(s)):
                prifix += s[j]
                maxi = max(maxi, prifix)
        return maxi
                

sol = Solution()
s = [4, -6, 2, 8]
print(sol.SumSubArr(s))