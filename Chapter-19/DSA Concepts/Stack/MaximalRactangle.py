class Solution:
    def LeftMinPrivious(self, Sarr):
        empty = [0] * len(Sarr[0])
        for i in range(len(Sarr)):
            for j in range(len(Sarr[0])):
                if Sarr[i][j] == 0:
                    empty[j] = 0
                else:
                    empty[j] += 1
            

                


sol = Solution()
arr = [
    [1, 0, 1, 0, 0],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1], 
    [1, 0, 0, 1, 0]
]
print(sol.LeftMinPrivious(arr))