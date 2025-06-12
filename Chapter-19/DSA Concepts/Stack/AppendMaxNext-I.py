class Solution():
    def popMaxNumber(self, Sarr):
        final = [-1] * len(Sarr)
        for i in range(len(Sarr)):
            for j in range(i, len(Sarr)):
                if Sarr[i] < Sarr[j]:
                    final[i] = Sarr[j]
                    break
        return final                 

sol = Solution()
Sarr = [8, 6, 4, 7, 4, 9, 10, 8, 12]
print(sol.popMaxNumber(Sarr))