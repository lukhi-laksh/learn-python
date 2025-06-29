class Solution:
    def maxSubArraySum(self, arr):
        maxi = -2**35 - 1
        prefix = 0
        for i in arr:
            prefix += i
            
            if prefix < 0:
                prefix = 0
            maxi = max(maxi, prefix)
            
        return maxi        
        
sol = Solution()
s = [2, 3, -8, 7, -1, 2, 3]
print(sol.maxSubArraySum(s))