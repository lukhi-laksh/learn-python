class Solution:
    def maxSubArraySum(self, arr):
        maxi = -2**35 - 1
        prefix = 0
        for i in arr:
            prefix += i
            
      
