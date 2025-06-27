class Solution(object):
    def SumSubArr(self, s):
        totalsum = 0
        presum = 0

        for i in s:
            totalsum += i
        for i in range(len(s) - 1):
            presum += s[i]
            if presum == (totalsum - presum):
                return True
        return False
            
            
sol = Solution()
s = [3, 4, -2, 5, 8, 20, -10, 8]
print(sol.SumSubArr(s))