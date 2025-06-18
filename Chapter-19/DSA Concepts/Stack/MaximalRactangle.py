class Solution:
    def LeftMinPrivious(self, Sarr):
        
        for i in range(len(Sarr)):
            for j in range(len(Sarr[0])):
                 if j == 0:
                     
                


sol = Solution()
arr = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1], 
    [1, 0, 0, 1, 0]
]
print(sol.LeftMinPrivious(arr))